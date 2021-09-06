# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename ZToThreeGamma_NANO_2016_cfg2.py --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --fileout file:process.root --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step NANO --filein process.root --era Run2_2016,run2_nanoAOD_106Xv1 --no_exec --mc -n 10
import FWCore.ParameterSet.Config as cms

import sys

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv1_cff import run2_nanoAOD_106Xv1

process = cms.Process('NANO',Run2_2016,run2_nanoAOD_106Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_0.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_1.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_10.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_100.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_101.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_102.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_103.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_104.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_105.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_106.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_107.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_108.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_109.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_11.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_110.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_111.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_112.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_113.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_114.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_115.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_116.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_117.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_118.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_119.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_12.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_120.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_121.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_122.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_123.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_124.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_125.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_126.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_127.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_128.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_129.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_13.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_130.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_131.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_132.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_133.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_134.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_135.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_136.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_137.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_138.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_139.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_14.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_140.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_141.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_142.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_143.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_144.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_145.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_146.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_147.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_148.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_149.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_15.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_150.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_151.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_152.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_153.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_154.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_155.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_156.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_157.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_158.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_159.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_16.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_160.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_161.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_162.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_163.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_164.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_165.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_166.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_167.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_168.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_169.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_17.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_170.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_171.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_172.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_173.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_174.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_175.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_176.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_177.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_178.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_179.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_18.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_180.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_181.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_182.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_183.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_185.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_186.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_187.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_188.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_189.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_19.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_190.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_191.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_192.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_193.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_194.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_195.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_196.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_197.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_198.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_199.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_2.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_20.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_21.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_22.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_23.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_24.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_25.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_26.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_27.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_28.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_29.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_3.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_30.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_31.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_32.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_33.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_34.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_35.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_36.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_37.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_38.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_39.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_4.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_40.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_41.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_42.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_43.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_44.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_45.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_46.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_47.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_48.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_49.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_5.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_50.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_51.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_52.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_53.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_54.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_55.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_56.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_57.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_58.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_59.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_6.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_60.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_61.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_62.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_63.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_64.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_65.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_66.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_67.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_68.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_69.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_7.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_70.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_71.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_72.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_73.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_74.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_75.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_76.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_77.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_78.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_79.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_8.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_80.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_81.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_82.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_83.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_84.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_85.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_86.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_87.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_88.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_89.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_9.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_90.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_91.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_92.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_93.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_94.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_95.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_96.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_97.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_98.root',
'file:/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/MINI/ZThreeGamma_99.root',
    ),

    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOEDMAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:process.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_preVFP_v11', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOEDMAODSIMoutput_step = cms.EndPath(process.NANOEDMAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOEDMAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
