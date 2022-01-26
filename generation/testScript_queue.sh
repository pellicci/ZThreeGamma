#!/bin/bash

HOMEDIR=/afs/cern.ch/user/p/pellicci/work/ZThreeGamma/Production/CMSSW_10_6_17_patch1/src/StandardModel/ZThreeGamma/generation
CMSSW_TO_USE=CMSSW_10_6_17_patch1
INPUTDIR=/eos/user/p/pellicci/ZThreeGamma_root/2017/signal/SIM
OUTPUTDIR=/eos/user/p/pellicci/ZThreeGamma_root/2017/signal/DIGI
PYTHONAME=ZToThreeGamma_DIGI_2017_cfg.py

NEVENTS=$1
FILENAME=$2

#this is necessary only if EOS access is required
export X509_USER_PROXY=/afs/cern.ch/user/p/pellicci/voms_proxy/x509up_u28550

export HOME=/afs/cern.ch/user/p/pellicci

if [ "$1" == "" ]; then
 echo "Specify number of events and base output file, eg: source testScript_queue.sh 50 test"
 exit 1;
fi
if [ "$2" == "" ]; then
 echo "Specify number of events and base output file, eg: source testScript_queue.sh 50 test"
 exit 1;
fi
OFFSET=$4
if [ "$4" == "" ]; then
 OFFSET=0
fi

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

export SCRAM_ARCH=slc7_amd64_gcc820
if [ -r $CMSSW_TO_USE/src ] ; then 
 echo release $CMSSW_TO_USE already exists
else
scram p CMSSW $CMSSW_TO_USE
fi
cd $CMSSW_TO_USE/src
eval `scram runtime -sh`
echo "check ld_library_path = $LD_LIBRARY_PATH"

cp $HOMEDIR/$PYTHONAME .
scram b

cat << EOF >> $PYTHONAME

from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()
EOF

jobNumber=$(($3+$OFFSET));

xrdcp $INPUTDIR/${FILENAME}_${jobNumber}.root .
cmsRun $PYTHONAME $NEVENTS ${FILENAME}_${jobNumber}.root
xrdcp process.root $OUTPUTDIR/${FILENAME}_${jobNumber}.root
