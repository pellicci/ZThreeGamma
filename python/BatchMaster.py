import sys, os, glob, subprocess, fileinput, math, datetime
from subprocess import PIPE, Popen

def get_current_time():
    now = datetime.datetime.now()
    currentTime = '{0:02d}{1:02d}{2:02d}_{3:02d}{4:02d}{5:02d}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    return currentTime

def make_directory(filePath, clear = True):
    if not os.path.exists(filePath):
        os.system('mkdir -p '+filePath)
    if clear and len(os.listdir(filePath)) != 0:
        os.system('rm '+filePath+'/*')

def inputFiles_from_txt(txt):
    ftxt = open(txt)
    inputFiles = ftxt.readlines()
    inputFiles = [f.strip() for f in inputFiles]
    return inputFiles

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

class JobConfig():
    '''Class for storing configuration for each dataset'''
    def __init__(self, dataset, nEvtPerJobIn1e6, year, isData, suffix, inputDBS = "global"):
        self._dataset   = dataset
        self._nEvtPerJobIn1e6 = nEvtPerJobIn1e6
        self._inputDBS = inputDBS
        
        # need to pass to executable
        self._year      = year
        self._isData    = isData
        self._suffix    = suffix


class BatchMaster():
    '''A tool for submitting batch jobs'''
    def __init__(self, analyzer, config_list, stage_dir, output_dir, executable='execBatch.sh'):
        self._current     = os.path.abspath('.')

        self._analyzer    = analyzer
        self._config_list = config_list
        self._stage_dir   = stage_dir
        self._output_dir  = output_dir

        self._executable  = executable
    
    def split_jobs_for_cfg(self, cfg):
        # query the root files using das commandline tool
        print "das query files"
        dasQuery_outFile = 'dasQuery_{}.txt'.format(cfg._suffix)
        if cfg._inputDBS == "global" :
            dasQuery_command = 'das_client -query="file dataset={}" > {}'.format(cfg._dataset, dasQuery_outFile)
        else :
            dasQuery_command = 'das_client -query="file dataset={} instance=prod/{}" > {}'.format(cfg._dataset, cfg._inputDBS, dasQuery_outFile)
        os.system(dasQuery_command)
        
        ftxt = open(dasQuery_outFile)
        fileList = ["root://cms-xrd-global.cern.ch/" + f.strip() for f in ftxt.readlines()]
        ftxt.close()
        nFiles = len(fileList)
        if nFiles <= 0:
            print "ERROR! No sample files are found! Exiting..."
            exit()
            
        # query number of events in the dataset
        print "das query number of events"
        if cfg._inputDBS == "global":
            output  = cmdline('das_client -query="dataset={} | grep dataset.nevents " '.format(cfg._dataset))
        else :
            output  = cmdline('das_client -query="dataset={} instance=prod/{} | grep dataset.nevents " '.format(cfg._dataset, cfg._inputDBS))
        nEvents = -1
        for l in output.splitlines():
            try: nEvents = int(l); break
            except: continue
        if nEvents < 0:
            print "ERROR! Unable to get the number of events for the dataset! Will use file based..."
            nJobs = nFiles
        else :
            # Split files to requested number.  Cannot exceed the number of files being run over.
            nJobs = int(math.ceil(nEvents/(1000000.0*cfg._nEvtPerJobIn1e6)))
            nJobs = nFiles if nJobs > nFiles else nJobs
        nFilesPerJob = int(math.ceil(float(nFiles)/float(nJobs)))
        sources = [ fileList[i:i+nFilesPerJob] for i in range(0, len(fileList), nFilesPerJob) ]

        print "DAS for dataset: ", cfg._dataset
        print "**************************************************"
        print "*  dataset: ", cfg._suffix
        print "*  {} events in {} files, raw_nJobs {}, nJobs {}".format(nEvents, nFiles, nJobs, len(sources))
        print "**************************************************"        
        print "save the DAS output to ", dasQuery_outFile

        # return a list with len=nJobs, For the given dataset
        return sources

    def make_batch(self, cfg):
        '''
        Prepares for submission.  Does the following:

        1. Generates input_files.txt with files to run over
        2. Write batch configuration file
        '''

        output_dir = self._output_dir
        print output_dir

        ## Writing the batch config file
        batch_tmp = open('batchJob_{0}.jdl'.format(cfg._suffix), 'w')
        batch_tmp.write('Should_Transfer_Files = YES\n')
        batch_tmp.write('WhenToTransferOutput  = ON_EXIT\n')
        batch_tmp.write('Notification          = Never\n')

        batch_tmp.write('\n')

        sources = self.split_jobs_for_cfg(cfg)
        for i, source in enumerate(sources):

            ## make file with list of inputs ntuples for the analyzer
            input_file = open('input_{}_{}.txt'.format(cfg._suffix, i+1), 'w')
            for s in source:
                input_file.write( s + "\n")
            input_file.close()

            ### set output directory
            batch_tmp.write('Arguments             = {0} {1} {2} {3} {4} {5}\n'.format(i+1, cfg._year, cfg._isData, cfg._suffix, output_dir, self._analyzer))
            batch_tmp.write('Executable            = {0}\n'.format(self._executable))
            batch_tmp.write('Transfer_Input_Files  = source.tar.gz, input_{0}_{1}.txt\n'.format(cfg._suffix, i+1))
            batch_tmp.write('Output                = reports/{0}_{1}_$(Cluster)_$(Process).stdout\n'.format(cfg._suffix, i+1))
            batch_tmp.write('Error                 = reports/{0}_{1}_$(Cluster)_$(Process).stderr\n'.format(cfg._suffix, i+1))
            batch_tmp.write('Log                   = reports/{0}_{1}_$(Cluster)_$(Process).log   \n'.format(cfg._suffix, i+1))
            batch_tmp.write('+JobFlavour           = \"workday\"\n')
            batch_tmp.write('Queue\n\n')

        batch_tmp.close()

    def submit_to_batch(self, doSubmit=True):
        '''
        Submits batch jobs to scheduler.  Currently only works
        for condor-based batch systems.
        '''
        #  set stage dir
        print 'Setting up stage directory...'
        self._stage_dir  = '{0}/{1}_{2}'.format(self._stage_dir, self._analyzer, get_current_time())
        make_directory(self._stage_dir, clear=False)

        # set output dir
        print 'Setting up output directory...'
        self._output_dir  = '{0}/{1}_{2}'.format(self._output_dir, self._analyzer, get_current_time())
        make_directory(self._output_dir, clear=False)

        # tar cmssw 
        print 'Creating tarball of current workspace in {0}'.format(self._stage_dir)
        if os.getenv('CMSSW_BASE') == '':
            print 'You must source the CMSSW environment you are working in...'
            exit()
        else:
            cmssw_version = os.getenv('CMSSW_BASE').split('/')[-1]
            if doSubmit:
                os.system('tar czf {0}/source.tar.gz --exclude=\'ZThree*.root\' -C $CMSSW_BASE/.. {1}'.format(self._stage_dir, cmssw_version))

        subprocess.call('cp {0} {1}'.format(self._executable, self._stage_dir), shell=True)
        os.chdir(self._stage_dir)
        make_directory('reports', clear=False)
    
        # submit
        for cfg in self._config_list:
            print "\n\n", cfg._suffix
            self.make_batch(cfg)
            if doSubmit:
                subprocess.call('condor_submit batchJob_{0}.jdl'.format(cfg._suffix), shell=True)
