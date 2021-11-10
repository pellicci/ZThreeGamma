#! /usr/bin/env python
import StandardModel.ZThreeGamma.BatchMaster as bm
import os, sys


# -----------------------------
# Specify parameters
# -----------------------------

executable = 'execBatch.sh'
analyzer   = 'run_ntuplizer.py'
stage_dir  = 'batch'
output_dir = '/eos/user/p/pellicci/ZThreeGamma_root/2016/skimprocess/'

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
    bm.JobConfig( dataset='/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD',
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
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=True, suffix='2016H_DoubleEG')
    ]

samplesDict['2016_MC'] = [ 
    bm.JobConfig( dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_DYJetsToLL'),
    bm.JobConfig( dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_DYJetsToLL'),
    bm.JobConfig( dataset='/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_ZGToLLG'),
    bm.JobConfig( dataset='/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_ZGToLLG'),
    bm.JobConfig( dataset='/DiPhotonJets_MGG-80toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_DiPhotonJets'),
    bm.JobConfig( dataset='/DiPhotonJets_MGG-80toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v2/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_DiPhotonJets'),
    bm.JobConfig( dataset='/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets40To100'),
    bm.JobConfig( dataset='/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets40To100'),
    bm.JobConfig( dataset='/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-4cores5k_106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets100To200'),
    bm.JobConfig( dataset='/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-4cores5k_106X_mcRun2_asymptotic_v15-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets100To200'),
    bm.JobConfig( dataset='/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets200To400'),
    bm.JobConfig( dataset='/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets200To400'),
    bm.JobConfig( dataset='/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets400To600'),
    bm.JobConfig( dataset='/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets400To600'),
    bm.JobConfig( dataset='/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v1_GJets600ToInf'),
    bm.JobConfig( dataset='/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='2016v2_GJets600ToInf')
    ]


# -----------------------------
# submit to batch
# -----------------------------
samplesToSubmit = samplesDict.keys()
samplesToSubmit.sort()
doYears = ["2016", "2017", "2018"]
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
