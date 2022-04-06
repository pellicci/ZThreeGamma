#!/usr/bin/env python
import os
import sys
import ROOT

inputfile = []
if len(sys.argv) > 3 :
    inputfile = [sys.argv[3]]
else :
    inputfile = ['/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2016/NANO/ZThreeGamma_NANO.root']

print inputfile

isData_string = sys.argv[1]
isData = False
if isData_string == "data" :
    isData = True
    print "Running on a data sample"
else :
    print "Running on a MC sample"

tmp_runningEra = sys.argv[2]
if "2016" in tmp_runningEra :
    myrunningEra = 0
elif "2017" in tmp_runningEra :
    myrunningEra = 2
elif "2018" in tmp_runningEra :
    myrunningEra = 3
print "Running era is ", myrunningEra

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

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
        self.N_Diphoton30_18 = 0.
        self.N_run3low = 0.
        self.N_run3high = 0.
        self.N_run3OR = 0.
        self.N_run3new = 0.
        pass
    def endJob(self):
        print "Total number of processed events = ", self.N_totevents
        print "Efficiency of double photon trigger = ", self.N_Diphoton30_18/self.N_totevents
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

        self.histcount.GetXaxis().SetBinLabel(1,"Initial eff")
        self.histcount.GetXaxis().SetBinLabel(2,"Trigger")
        self.histcount.GetXaxis().SetBinLabel(3,"Muon veto")
        self.histcount.GetXaxis().SetBinLabel(4,"N_{#gamma} > 2")
        self.histcount.GetXaxis().SetBinLabel(5,"E_{T,#gamma} cuts")
        self.histcount.GetXaxis().SetBinLabel(6,"m_{#gamma#gamma} > 40 or < 110")
        self.histcount.GetXaxis().SetBinLabel(7,"Loose+Loose")
        self.histcount.GetXaxis().SetBinLabel(8,"Pixel seed veto")
        self.histcount.GetXaxis().SetBinLabel(9,"m_{XY} < 100")

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

        if len(photons) > 2 :
            ph1_4mom = photons[0].p4()
            ph2_4mom = photons[1].p4()
            ph3_4mom = photons[2].p4()

            ph_3mass = (ph1_4mom + ph2_4mom + ph3_4mom).M()

            ########################################
            #These are just counters for signal studies
            if (ph1_4mom.Pt() > 20. and ph2_4mom.Pt() > 20. and ph3_4mom.Pt() > 20.) :
                self.N_run3low += 1

            if (ph1_4mom.Pt() > 30. and ph2_4mom.Pt() > 30. and ph3_4mom.Pt() > 10.) :
                self.N_run3high += 1

            if (ph1_4mom.Pt() > 20. and ph2_4mom.Pt() > 20. and ph3_4mom.Pt() > 20.) or (ph1_4mom.Pt() > 30. and ph2_4mom.Pt() > 30. and ph3_4mom.Pt() > 10.) :
                self.N_run3OR += 1

            if (ph1_4mom.Pt() > 20. and ph2_4mom.Pt() > 20. and ph3_4mom.Pt() > 10. and ph_3mass > 55.) :
                self.N_run3new += 1

        if self.runningEra < 2 :
            if HLT.Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55 or HLT.Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55:
                self.N_Diphoton30_18 += 1

        ########################################

        ####here starts the actual selection
        if self.runningEra < 2 and not (HLT.Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55 or HLT.Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55) :
            return False

        if self.runningEra == 2 and not HLT.Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_PixelVeto_Mass55 :
            return False

        self.histcount.Fill(1)

        N_muonscount = 0
        for muoncount in xrange(len(muons)) :
            if not muons[muoncount].isGlobal :
                continue
            N_muonscount = N_muonscount + 1
        if N_muonscount > 0 :
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

        if (ph1_4mom.Pt() < 30. or ph2_4mom.Pt() < 18. or ph3_4mom.Pt() < 10.) : 
            return False
        self.histcount.Fill(4)

        if (ph1_4mom + ph2_4mom + ph3_4mom).M() < 60. :
            return False
        self.histcount.Fill(5)

        if not (photons[0].mvaID_WP90 and photons[1].mvaID_WP90 and photons[2].mvaID_WP90) :
            return False
        self.histcount.Fill(6)

        if (photons[0].pixelSeed or photons[1].pixelSeed or photons[2].pixelSeed) :
            return False
        self.histcount.Fill(7)

        Fourmom_12 = ph1_4mom + ph2_4mom
        Fourmom_13 = ph1_4mom + ph3_4mom
        Fourmom_23 = ph2_4mom + ph3_4mom

        if Fourmom_12.M() > 110. or Fourmom_13.M() > 110. or Fourmom_23.M() > 110. :
            return False
        self.histcount.Fill(8)

        self.out.fillBranch("M_threegam",ph_3mass)

        return True

if isData :
    p=PostProcessor(".",inputfile,"",modules=[exampleProducer(myrunningEra)],provenance=True,fwkJobReport=True,outputbranchsel="keep_and_drop.txt")
    p.run()
else :
    if myrunningEra < 2 :
        p=PostProcessor(".",inputfile,"",modules=[exampleProducer(myrunningEra),puAutoWeight_2016()],provenance=True,fwkJobReport=True,outputbranchsel="keep_and_drop.txt")
    elif myrunningEra == 2 :
        p=PostProcessor(".",inputfile,"",modules=[exampleProducer(myrunningEra),puAutoWeight_2017()],provenance=True,fwkJobReport=True,outputbranchsel="keep_and_drop.txt")
    p.run()


print "DONE"
