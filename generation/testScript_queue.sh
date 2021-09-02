#!/bin/bash

HOMEDIR=/afs/cern.ch/user/p/pellicci/work/ZThreeGamma/Production/CMSSW_10_6_17_patch1/src/StandardModel/ZThreeGamma/generation
CMSSW_TO_USE=CMSSW_10_6_17
INPUTDIR=/eos/user/p/pellicci/ZThreeGamma_root/2016/SIM
OUTPUTDIR=/eos/user/p/pellicci/ZThreeGamma_root/2016/DIGI
PYTHONAME=ZToThreeGamma_DIGI_2016_cfg.py

#this is necessary only if EOS access is required
export X509_USER_PROXY=/afs/cern.ch/user/p/pellicci/voms_proxy/x509up_u28550

voms-proxy-info -all
voms-proxy-info -all -file $X509_USER_PROXY

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

NEVENTS=$1
OUTPUT=$2

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

xrdcp $INPUTDIR/ZThreeGamma_${jobNumber}.root .

cmsRun $PYTHONAME $NEVENTS ZThreeGamma_${jobNumber}.root

xrdcp process.root $OUTPUTDIR/${OUTPUT}_${jobNumber}.root
