#!/usr/bin/env python
import os
import sys
import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *

class exampleProducer(Module):
    def __init__(self, runningEra):
        self.runningEra = runningEra
        pass
    def beginJob(self):
        self.N_totevents = 0.
        self.N_Ph36_Id90_HE10_IsoM = 0.
        self.N_Diphoton30_18_PV = 0.
        self.N_ORtrigger = 0.
        self.N_run3low = 0.
        self.N_run3high = 0.
        self.N_run3OR = 0.
        self.N_run3new = 0.
        pass
    def endJob(self):
        print "Total number of processed events = ", self.N_totevents
        print "Efficiency of single lepton trigger = ", self.N_Ph36_Id90_HE10_IsoM/self.N_totevents
        print "Efficiency of double lepton trigger = ", self.N_Diphoton30_18_PV/self.N_totevents
        print "Efficiency of the OR = ", self.N_ORtrigger/self.N_totevents
        print "Efficiency for run 3 lower trigger = ", self.N_run3low/self.N_totevents
        print "Efficiency for run 3 higher trigger = ", self.N_run3high/self.N_totevents
        print "Efficiency for run 3 OR = ", self.N_run3OR/self.N_totevents
        print "Efficiency for run 3 proposal = ", self.N_run3new/self.N_totevents
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("M_threegam",  "F");
        self.histcount = ROOT.TH1F("histocount","Counter of passed events",10,-0.5,9.5)
        self.photoncount = ROOT.TH1F("photoncount","Counter of passed photons",10,-0.5,9.5)
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        outputFile.cd()
        self.histcount.Write()
        self.photoncount.Write()
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        self.N_totevents += 1
        self.histcount.Fill(0)

        HLT = Object(event, "HLT")
        electrons = Collection(event, "Electron")
        photons = Collection(event, "Photon")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        PuppiMET = Object(event, "PuppiMET")

        ph_3mass = 0.

        if (len(photons) > 2) :
            ph1_4mom = photons[0].p4()
            ph2_4mom = photons[1].p4()
            ph3_4mom = photons[2].p4()

            ph_3mass = (ph1_4mom + ph2_4mom + ph3_4mom).M()

            if (ph1_4mom.Pt() > 20. and ph2_4mom.Pt() > 20. and ph3_4mom.Pt() > 20.) :
                self.N_run3low += 1

            if (ph1_4mom.Pt() > 30. and ph2_4mom.Pt() > 30. and ph3_4mom.Pt() > 10.) :
                self.N_run3high += 1

            if (ph1_4mom.Pt() > 20. and ph2_4mom.Pt() > 20. and ph3_4mom.Pt() > 20.) or (ph1_4mom.Pt() > 30. and ph2_4mom.Pt() > 30. and ph3_4mom.Pt() > 10.) :
                self.N_run3OR += 1

            if (ph1_4mom.Pt() > 20. and ph2_4mom.Pt() > 20. and ph3_4mom.Pt() > 10. and ph_3mass > 55.) :
                self.N_run3new += 1

        if HLT.Photon36_R9Id90_HE10_IsoM :
            self.N_Ph36_Id90_HE10_IsoM += 1

        if HLT.Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55 :
            self.N_Diphoton30_18_PV += 1

        if (HLT.Photon36_R9Id90_HE10_IsoM or HLT.Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55) :
            self.N_ORtrigger += 1

        ####here starts the actual selection
        if self.runningEra == 0 and not (HLT.Photon36_R9Id90_HE10_IsoM or HLT.Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55) :
            return False
        self.histcount.Fill(1)

        if len(muons) > 0 :
            return False
        self.histcount.Fill(2)

        if len(photons) < 3 :
            return False
        self.histcount.Fill(3)


        N_photons_select = 0.
        for photoncount in xrange(len(photons)) :
            if not photons[photoncount].mvaID_WP90 :
                continue
            if photons[photoncount].p4().Pt() < 5. :
                continue

            N_photons_select += 1

        self.photoncount.Fill(N_photons_select)

        ph1_4mom = photons[0].p4()
        ph2_4mom = photons[1].p4()
        ph3_4mom = photons[2].p4()

        if (ph1_4mom.Pt() < 30. or ph2_4mom.Pt() < 18. or ph3_4mom.Pt() < 5.) : 
            return False
        self.histcount.Fill(4)

        if (ph1_4mom + ph2_4mom + ph3_4mom).M() < 60. :
            return False
        self.histcount.Fill(5)

        if not (photons[0].mvaID_WP80 and photons[1].mvaID_WP90 and photons[2].mvaID_WP90) :
            return False
        self.histcount.Fill(6)

        if (photons[0].pixelSeed or photons[1].pixelSeed or photons[2].pixelSeed) :
            return False
        self.histcount.Fill(7)

        self.out.fillBranch("M_threegam",ph_3mass)

        return True

inputfile = ['/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/NANO/ZThreeGamma_NANO.root']
#inputfile = ['/afs/cern.ch/user/p/pellicci/work/ZThreeGamma/CMSSW_10_6_27/src/StandardModel/ZThreeGamma/test/4C08107E-ECEF-C647-B3CA-2F1248A41A60.root']
#p=PostProcessor(".",inputfile,"",modules=[exampleProducer(),puAutoWeight_2016()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
p=PostProcessor(".",inputfile,"",modules=[exampleProducer(0),puAutoWeight_2016()],provenance=True,fwkJobReport=True,outputbranchsel="keep_and_drop.txt")

p.run()

print "DONE"
