#! /usr/bin/env python
import StandardModel.ZThreeGamma.BatchMaster as bm
import os, sys


# -----------------------------
# Specify parameters
# -----------------------------

executable = 'execBatch.sh'
analyzer   = 'run_ntuplizer.py'
stage_dir  = 'batch'
output_dir = '/eos/user/p/pellicci/ZThreeGamma_root/2016/data/'

# -----------------------------
# Set job configurations.  
# -----------------------------
samplesDict = {}

nEvtPerJob = 1 # faster jobs, # in unit of 1e6 , 5-10 are good settings. 

#################################################
#                                               #
#---------------  Running data   ---------------#
#                                               #
#################################################
# dataset, nEvtPerJobIn1e6, year, isData, suffix

# Single Electron
samplesDict['2016'] = [ 
    bm.JobConfig( dataset='/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016Bv1_DoubleEG'),
    bm.JobConfig( dataset='/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016Bv2_DoubleEG'),
    bm.JobConfig( dataset='/DoubleEG/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016C_DoubleEG'),
    bm.JobConfig( dataset='/DoubleEG/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016D_DoubleEG'),
    bm.JobConfig( dataset='/DoubleEG/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016E_DoubleEG'),
    bm.JobConfig( dataset='/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016FHIPM_DoubleEG'),
    bm.JobConfig( dataset='/DoubleEG/Run2016F-UL2016_MiniAODv1_NanoAODv2-v2/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016F_DoubleEG'),
    bm.JobConfig( dataset='/DoubleEG/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016G_DoubleEG'),
    bm.JobConfig( dataset='/DoubleEG/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016H_DoubleEG'),
    bm.JobConfig( dataset='/SinglePhoton/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016Bv1_SingleEG'),
    bm.JobConfig( dataset='/SinglePhoton/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016Bv2_SingleEG'),
    bm.JobConfig( dataset='/SinglePhoton/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016C_SingleEG'),
    bm.JobConfig( dataset='/SinglePhoton/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016D_SingleEG'),
    bm.JobConfig( dataset='/SinglePhoton/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016E_SingleEG'),
    bm.JobConfig( dataset='/SinglePhoton/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016FHIPM_SingleEG'),
    bm.JobConfig( dataset='/SinglePhoton/Run2016F-UL2016_MiniAODv1_NanoAODv2-v3/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016F_SingleEG'),
    bm.JobConfig( dataset=' /SinglePhoton/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016G_SingleEG'),
    bm.JobConfig( dataset='/SinglePhoton/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016H_SingleEG')
    ]

# -----------------------------
# submit to batch
# -----------------------------
samplesToSubmit = samplesDict.keys()
samplesToSubmit.sort()
configs = []

for s in samplesToSubmit:
    configs += samplesDict[s]

batchMaster = bm.BatchMaster(
    analyzer    = analyzer,
    config_list = configs, 
    stage_dir   = stage_dir,
    output_dir  = output_dir,
    executable  = executable,
)

#ensure there's a symbolic link 'batch' to put the tarball in
if not os.path.exists("batch") :
    os.symlink("/afs/cern.ch/user/p/pellicci/nobackup/batch", "batch")
    print "Created symbolic link to ~/nobackup/batch"

batchMaster.submit_to_batch(doSubmit=True)
