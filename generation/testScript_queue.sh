#!/bin/bash

HOMEDIR=/afs/cern.ch/user/p/pellicci/work/ZThreeGamma/CMSSW_10_6_27/src/StandardModel/ZThreeGamma/generation
CMSSW_TO_USE=CMSSW_10_6_17_patch1
INPUTDIR=/eos/user/p/pellicci/ZThreeGamma_root/2016/GGG/postAPV/HLT/
OUTPUTDIR=/eos/user/p/pellicci/ZThreeGamma_root/2016/GGG/postAPV/RECO/
PYTHONAME=GGG_LHEGEN_2016_postAPV_v9_cfg.py

echo "First argument is $1"

#this is necessary only if EOS access is required
export X509_USER_PROXY=/afs/cern.ch/user/p/pellicci/voms_proxy/x509up_u28550
export HOME=/afs/cern.ch/user/p/pellicci

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

cp $HOMEDIR/$PYTHONAME config_cfg.py
scram b

cat << EOF >> $PYTHONAME

from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()
EOF

jobNumber=$1;

echo "jobnumber is $jobNumber"

#SIM 2016 preAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent RAWSIM --datatier GEN-SIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step SIM --geometry DB:Extended --filein file:processIN.root --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n -1
#DIGI 2016 preAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent PREMIXRAW --datatier GEN-SIM-DIGI --fileout file:process.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX" --conditions 106X_mcRun2_asymptotic_preVFP_v8 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --filein file:processIN.root --datamix PreMix --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n -1
#HLT 2016 preAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent RAWSIM --outputCommand "keep *_mix_*_*,keep *_genPUProtons_*_*" --datatier GEN-SIM-RAW --inputCommands "keep *","drop *_*_BMTF_*","drop *PixelFEDChannel*_*_*_*" --fileout file:process.root --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:25ns15e33_v4 --geometry DB:Extended --filein file:processIN.root --era Run2_2016 --no_exec --mc -n -1
#RECO 2016 preAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent AODSIM --datatier AODSIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_preVFP_v8 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --filein file:processIN.root --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n -1
#MINI 2016 preAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent MINIAODSIM --datatier MINIAODSIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --filein file:processIN.root --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n -1
#NANO 2016 preAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent NANOAODSIM --datatier NANOAODSIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step NANO --filein file:processIN.root --era Run2_2016_HIPM,run2_nanoAOD_106Xv2 --no_exec --mc -n -1

#SIM 2016 postAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent RAWSIM --datatier GEN-SIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step SIM --geometry DB:Extended --filein file:processIN.root --era Run2_2016 --runUnscheduled --no_exec --mc -n -1
#DIGI 2016 postAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent PREMIXRAW --datatier GEN-SIM-DIGI --fileout file:process.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX" --conditions 106X_mcRun2_asymptotic_v13 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --filein file:processIN.root --datamix PreMix --era Run2_2016 --runUnscheduled --no_exec --mc -n -1
#HLT 2016 postAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent RAWSIM --outputCommand "keep *_mix_*_*,keep *_genPUProtons_*_*" --datatier GEN-SIM-RAW --inputCommands "keep *","drop *_*_BMTF_*","drop *PixelFEDChannel*_*_*_*" --fileout file:process.root --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:25ns15e33_v4 --geometry DB:Extended --filein file:processIN.root --era Run2_2016 --no_exec --mc -n -1
#RECO 2016 postAPV_v9
cmsDriver.py  --python_filename config_cfg.py --eventcontent AODSIM --datatier AODSIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_v13 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --filein file:processIN.root --era Run2_2016 --runUnscheduled --no_exec --mc -n -1
#MINI 2016 postAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent MINIAODSIM --datatier MINIAODSIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_v17 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --filein file:processIN.root --era Run2_2016 --runUnscheduled --no_exec --mc -n -1
#NANO 2016 preAPV_v9
#cmsDriver.py  --python_filename config_cfg.py --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_v17 --step NANO --filein file:processIN.root --era Run2_2016,run2_nanoAOD_106Xv2 --no_exec --mc -n -1


xrdcp $INPUTDIR/process_${jobNumber}.root processIN.root
cmsRun config_cfg.py
xrdcp process.root $OUTPUTDIR/process_${jobNumber}.root
