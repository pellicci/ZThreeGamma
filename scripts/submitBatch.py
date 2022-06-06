#! /usr/bin/env python
import StandardModel.ZThreeGamma.BatchMaster as bm
import os, sys


# -----------------------------
# Specify parameters
# -----------------------------

executable = 'execBatch.sh'
analyzer   = 'run_ntuplizer.py'
stage_dir  = 'batch'
output_dir = '/eos/user/p/pellicci/ZThreeGamma_root/skimprocess/'

# -----------------------------
# Set job configurations.  
# -----------------------------
samplesDict = {}

nEvtPerJob = 0.4 # faster jobs, # in unit of 1e6 , 5-10 are good settings. 

#################################################
#                                               #
#---------------  Running data   ---------------#
#                                               #
#################################################
# dataset, nEvtPerJobIn1e6, year, isData, suffix

# Single Electron
samplesDict['2016'] = [ 
#    bm.JobConfig( dataset='/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016Bv1_DoubleEG'),
#    bm.JobConfig( dataset='/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v3/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016Bv2_DoubleEG'),
#    bm.JobConfig( dataset='/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016C_DoubleEG'),
#    bm.JobConfig( dataset='/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016D_DoubleEG'),
#    bm.JobConfig( dataset='/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016E_DoubleEG'),
#    bm.JobConfig( dataset='/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016FHIPM_DoubleEG'),
#    bm.JobConfig( dataset='/DoubleEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016F_DoubleEG'),
#    bm.JobConfig( dataset='/DoubleEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016G_DoubleEG'),
#    bm.JobConfig( dataset='/DoubleEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016H_DoubleEG')
    ]

samplesDict['2017'] = [
    # bm.JobConfig( dataset='/DoubleEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
    #     nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=True, suffix='2017B_DoubleEG'),
    # bm.JobConfig( dataset='/DoubleEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
    #     nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=True, suffix='2017C_DoubleEG'),
    # bm.JobConfig( dataset='/DoubleEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
    #     nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=True, suffix='2017D_DoubleEG'),
    # bm.JobConfig( dataset='/DoubleEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
    #     nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=True, suffix='2017E_DoubleEG'),
    # bm.JobConfig( dataset='/DoubleEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
    #     nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=True, suffix='2017F_DoubleEG')
    ]

samplesDict['2018'] = [ 
    bm.JobConfig( dataset='/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=True, suffix='2018A_DoubleEG'),
    bm.JobConfig( dataset='/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=True, suffix='2018B_DoubleEG'),
    bm.JobConfig( dataset='/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=True, suffix='2018C_DoubleEG'),
    bm.JobConfig( dataset='/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=True, suffix='2018D_DoubleEG')
    ]

samplesDict['2016_MC'] = [ 
#    bm.JobConfig( dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_DYJetsToLL'),
#    bm.JobConfig( dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_DYJetsToLL'),
#    bm.JobConfig( dataset='/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_ZGToLLG'),
#    bm.JobConfig( dataset='/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_ZGToLLG'),
#    bm.JobConfig( dataset='/DiPhotonJets_MGG-80toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_DiPhotonJets'),
#    bm.JobConfig( dataset='/DiPhotonJets_MGG-80toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_DiPhotonJets'),
#    bm.JobConfig( dataset='/DiPhotonJetsBox_M40_80-sherpa/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_DiPhotonJets40'),
    bm.JobConfig( dataset='/DiPhotonJetsBox_M40_80-sherpa/pellicci-crab_ZThreeGamma_Diphoton_2016v2-00000000000000000000000000000000/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_DiPhotonJets40', inputDBS='phys03')
#    bm.JobConfig( dataset='/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets40To100'),
#    bm.JobConfig( dataset='/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets40To100'),
#    bm.JobConfig( dataset='/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets100To200'),
#    bm.JobConfig( dataset='/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-4cores5k_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets100To200'),
#    bm.JobConfig( dataset='/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets200To400'),
#    bm.JobConfig( dataset='/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets200To400'),
#    bm.JobConfig( dataset='/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets400To600'),
#    bm.JobConfig( dataset='/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets400To600'),
#    bm.JobConfig( dataset='/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets600ToInf'),
#    bm.JobConfig( dataset='/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets600ToInf')
    ]

samplesDict['2017_MC'] = [ 
#    bm.JobConfig( dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='2017_DYJetsToLL'),
#    bm.JobConfig( dataset='/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='2017_ZGToLLG'),
#    bm.JobConfig( dataset='/DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='2017_DiPhotonJets'),
    bm.JobConfig( dataset='/DiPhotonJetsBox_M40_80-sherpa/pellicci-crab_ZThreeGamma_Diphoton_2017-00000000000000000000000000000000/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='2017_DiPhotonJets40', inputDBS='phys03')
#    bm.JobConfig( dataset='/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='2017_GJets100To200'),
#    bm.JobConfig( dataset='/GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='2017_GJets200To400'),
#    bm.JobConfig( dataset='/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='2017_GJets400To600'),
#    bm.JobConfig( dataset='/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM',
#        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='2017_GJets600ToInf')
    ]

samplesDict['2018_MC'] = [ 
    bm.JobConfig( dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='2018_DYJetsToLL'),
    bm.JobConfig( dataset='/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='2018_ZGToLLG'),
    bm.JobConfig( dataset='/DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='2018_DiPhotonJets'),
    bm.JobConfig( dataset='/DiPhotonJetsBox_M40_80-sherpa/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='2018_DiPhotonJets40'),
    bm.JobConfig( dataset='/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='2018_GJets100To200'),
    bm.JobConfig( dataset='/GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='2018_GJets200To400'),
    bm.JobConfig( dataset='/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='2018_GJets400To600'),
    bm.JobConfig( dataset='/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='2018_GJets600ToInf')
    ]

# -----------------------------
# submit to batch
# -----------------------------
samplesToSubmit = samplesDict.keys()
samplesToSubmit.sort()
#doYears = ["2016", "2017", "2018"]
doYears = ["2016","2017"]
configs = []

for s in samplesToSubmit:
    if s[:4] in doYears:
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
