#!/bin/bash

FILENUMBER=$1
SAMPLENAME=$2

echo "Filenumber is $FILENUMBER"
echo "Samplename is $SAMPLENAME"

HOMEDIR=/afs/cern.ch/user/p/pellicci/work/ZThreeGamma/CMSSW_10_6_27/src/StandardModel/ZThreeGamma/test
CMSSW_TO_USE=CMSSW_10_6_27
PYTHONAME=run_ntuplizer.py
OUTPUTDIR=/eos/user/p/pellicci/ZThreeGamma_root/2016/backgrounds/${SAMPLENAME}
INPUTFILENAME=lists_files/mc_2016NANOAODAPV/${SAMPLENAME}.txt
PROCESSNAME=ZThreeGamma_${SAMPLENAME}

#this is necessary only if EOS access is required
export X509_USER_PROXY=/afs/cern.ch/user/p/pellicci/voms_proxy/x509up_u28550

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

git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools

cp $HOMEDIR/$PYTHONAME .
cp $HOMEDIR/keep_and_drop.txt .
scram b

INPUTFILE=`sed -n ${FILENUMBER}p ${HOMEDIR}/${INPUTFILENAME}`

echo $INPUTFILE

CWD=`pwd`

echo $CWD

xrdcp root://cmsxrootd.fnal.gov/${INPUTFILE} process.root
python run_ntuplizer.py ${CWD}/process.root
xrdcp tree.root $OUTPUTDIR/${PROCESSNAME}_${FILENUMBER}.root
