#!/usr/bin/env python
import os
import sys
import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import correctionlib

inputfile = []
if len(sys.argv) > 3 :
    inputfile = [sys.argv[3]]
else :
    inputfile = ['/afs/cern.ch/user/p/pellicci/cernbox/ZThreeGamma_root/2018/signal/NANO/ZThreeGamma_NANO_2018.root']

print inputfile

isData_string = sys.argv[1]
isData = False
if isData_string == "data" :
    isData = True
    print "Running on a data sample"
else :
    print "Running on a MC sample"

myrunningEra = -1
tmp_runningEra = sys.argv[2]
if "2016" in tmp_runningEra :
    myrunningEra = 0
elif "2017" in tmp_runningEra :
    myrunningEra = 2
elif "2018" in tmp_runningEra :
    myrunningEra = 3
elif "2022" in tmp_runningEra :
    myrunningEra = 4
print "Running era is ", myrunningEra

ROOT.PyConfig.IgnoreCommandLineOptions = True

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

        if self.runningEra > 2 and not HLT.Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto :
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

        if (ph1_4mom.Pt() < 32. or ph2_4mom.Pt() < 20. or ph3_4mom.Pt() < 10.) : 
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

        #trigger offline preselection
        isEBphot1 = True if abs(ph1_4mom.Eta()) < 1.48 else False
        isEBphot2 = True if abs(ph2_4mom.Eta()) < 1.48 else False

        if photons[0].hoe > 0.1 or photons[1].hoe > 0.1 :
            return False
        if (isEBphot1 and photons[0].r9 < 0.85) or (not isEBphot1 and photons[0].r9 < 0.9) :
            return False
        if (isEBphot2 and photons[1].r9 < 0.85) or (not isEBphot2 and photons[1].r9 < 0.9) :
            return False
        if abs(ph1_4mom.Eta()) > 2.5 or abs(ph2_4mom.Eta()) > 2.5 or abs(ph3_4mom.Eta()) > 2.5 :
            return False
        if (isEBphot1 and photons[0].sieie > 0.015) or (not isEBphot1 and photons[0].sieie > 0.035) :
            return False
        if (isEBphot2 and photons[1].sieie > 0.015) or (not isEBphot2 and photons[1].sieie > 0.035) :
            return False

        #if Fourmom_12.M() > 110. or Fourmom_13.M() > 110. or Fourmom_23.M() > 110. :
        #    return False
        #self.histcount.Fill(8)

        self.out.fillBranch("M_threegam",ph_3mass)

        return True

p=PostProcessor(".",inputfile,"",modules=[exampleProducer(myrunningEra)],provenance=True,fwkJobReport=True,outputbranchsel="keep_and_drop.txt")
p.run()

print "DONE"
