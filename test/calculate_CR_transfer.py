#!/usr/bin/env python

import ROOT
import argparse

p = argparse.ArgumentParser(description='Select whether to fill the histograms after pre-selection or selection')
p.add_argument('runningEra_option', help='Type <<0>> for 2016, <<2>> for 2017, <<3>> for 2018')
args = p.parse_args()

runningEra = int(args.runningEra_option)

if runningEra == 0 :
	fileCR1 = ROOT.TFile("histos/ZThreeGamma_CR1_0.root")
	fileCR2 = ROOT.TFile("histos/ZThreeGamma_CR2_0.root")
	fileCR3 = ROOT.TFile("histos/ZThreeGamma_CR3_0.root")
elif runningEra == 2 :
	fileCR1 = ROOT.TFile("histos/ZThreeGamma_CR1_2.root")
	fileCR2 = ROOT.TFile("histos/ZThreeGamma_CR2_2.root")
	fileCR3 = ROOT.TFile("histos/ZThreeGamma_CR3_2.root")

h_CR1_phot2Et_low12 = fileCR1.Get("h_phot2_ET_low12")
h_CR2_phot3Et_low12 = fileCR2.Get("h_phot3_ET_low12")
h_CR3_phot2Et_low12 = fileCR3.Get("h_phot2_ET_low12")
h_CR3_phot3Et_low12 = fileCR3.Get("h_phot3_ET_low12")

h_CR1_phot2Et_high12 = fileCR1.Get("h_phot2_ET_high12")
h_CR2_phot3Et_high12 = fileCR2.Get("h_phot3_ET_high12")
h_CR3_phot2Et_high12 = fileCR3.Get("h_phot2_ET_high12")
h_CR3_phot3Et_high12 = fileCR3.Get("h_phot3_ET_high12")

h_CR1_phot2Et = fileCR1.Get("h_phot2_ET")
h_CR2_phot1Et = fileCR2.Get("h_phot1_ET")
h_CR2_phot3Et = fileCR2.Get("h_phot3_ET")
h_CR3_phot1Et = fileCR3.Get("h_phot1_ET")
h_CR3_phot2Et = fileCR3.Get("h_phot2_ET")
h_CR3_phot3Et = fileCR3.Get("h_phot3_ET")

h_CR1_phot2Et_low12.Rebin(10)
h_CR2_phot3Et_low12.Rebin(10)
h_CR3_phot2Et_low12.Rebin(10)
h_CR3_phot3Et_low12.Rebin(10)
h_CR1_phot2Et_high12.Rebin(10)
h_CR2_phot3Et_high12.Rebin(10)
h_CR3_phot2Et_high12.Rebin(10)
h_CR3_phot3Et_high12.Rebin(10)
h_CR1_phot2Et.Rebin(10)
h_CR2_phot1Et.Rebin(10)
h_CR2_phot3Et.Rebin(10)
h_CR3_phot1Et.Rebin(10)
h_CR3_phot2Et.Rebin(10)
h_CR3_phot3Et.Rebin(10)

h_CR1_phot2Et_low12.Divide(h_CR3_phot2Et_low12)
h_CR2_phot3Et_low12.Divide(h_CR3_phot3Et_low12)

h_CR1_phot2Et_high12.Divide(h_CR3_phot2Et_high12)
h_CR2_phot3Et_high12.Divide(h_CR3_phot3Et_high12)

h_CR1_phot2Et.Divide(h_CR3_phot2Et)
h_CR2_phot1Et.Divide(h_CR3_phot1Et)
h_CR2_phot3Et.Divide(h_CR3_phot3Et)

canva = ROOT.TCanvas("canvas","",200,106,600,600)
canva.Divide(2,1)
canva.cd(1)
h_CR1_phot2Et_low12.Draw("E1")
canva.cd(2)
h_CR2_phot3Et_low12.Draw("E1")

if runningEra == 0 :
	canva.SaveAs("plots/CRfrac_photEt_0.gif")
elif runningEra == 2 :
	canva.SaveAs("plots/CRfrac_photEt_2.gif")

h_CR1_phot2Et_low12.SetName("CR1_fraction_phot2ET_low12")
h_CR2_phot3Et_low12.SetName("CR2_fraction_phot3ET_low12")
h_CR1_phot2Et_high12.SetName("CR1_fraction_phot2ET_high12")
h_CR2_phot3Et_high12.SetName("CR2_fraction_phot3ET_high12")
h_CR1_phot2Et.SetName("CR1_fraction_phot2ET")
h_CR2_phot1Et.SetName("CR2_fraction_phot1ET")
h_CR2_phot3Et.SetName("CR2_fraction_phot3ET")

if runningEra == 0 :
	fOut = ROOT.TFile("histos/CRfraction_0.root","RECREATE")
elif runningEra == 2 :
	fOut = ROOT.TFile("histos/CRfraction_2.root","RECREATE")

fOut.cd()

h_CR1_phot2Et_low12.Write()
h_CR2_phot3Et_low12.Write()
h_CR1_phot2Et_high12.Write()
h_CR2_phot3Et_high12.Write()
h_CR1_phot2Et.Write()
h_CR2_phot1Et.Write()
h_CR2_phot3Et.Write()

fOut.Close()
