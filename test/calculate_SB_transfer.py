#!/usr/bin/env python3

import ROOT
import argparse

ROOT.gROOT.SetBatch(True)

fileSB   = ROOT.TFile("histos/ZThreeGamma_SB.root")
filedata = ROOT.TFile("histos/ZThreeGamma_data.root")

h_SB_phot1Et = fileSB.Get("h_phot1_ET")
h_data_phot1Et = filedata.Get("h_phot1_ET")

h_SB_phot12Et = fileSB.Get("h_phot12_ET")
h_data_phot12Et = filedata.Get("h_phot12_ET")

h_SB_phot1Et.Rebin(2)
h_data_phot1Et.Rebin(2)

h_SB_phot12Et.Rebin2D(2)
h_data_phot12Et.Rebin2D(2)

h_data_phot1Et.Divide(h_SB_phot1Et)
h_data_phot12Et.Divide(h_SB_phot12Et)

h_data_phot1Et.SetName("h_data_phot1Et")
h_data_phot12Et.SetName("h_data_phot12Et")

canva = ROOT.TCanvas("canvas","",200,106,600,600)
canva.cd()
h_data_phot12Et.Draw("E1")
canva.SaveAs("plots/SBfrac_phot12Et.gif")

fOut = ROOT.TFile("histos/SBfraction.root","RECREATE")
fOut.cd()
h_data_phot1Et.Write()
h_data_phot12Et.Write()
fOut.Close()

print("###############")
print("Calculated transfer factors!")
print("###############")
