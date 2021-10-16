import ROOT

fileCR1 = ROOT.TFile("histos/ZThreeGamma_CR1.root")
fileCR2 = ROOT.TFile("histos/ZThreeGamma_CR2.root")
fileCR3 = ROOT.TFile("histos/ZThreeGamma_CR3.root")

h_CR1_phot2Et_low12 = fileCR1.Get("h_phot2_ET_low12")
h_CR2_phot3Et_low12 = fileCR2.Get("h_phot3_ET_low12")
h_CR3_phot2Et_low12 = fileCR3.Get("h_phot2_ET_low12")
h_CR3_phot3Et_low12 = fileCR3.Get("h_phot3_ET_low12")

h_CR2_phot3Et_high12 = fileCR2.Get("h_phot3_ET_high12")
h_CR3_phot3Et_high12 = fileCR3.Get("h_phot3_ET_high12")

h_CR1_phot2Et_low12.Rebin(4)
h_CR2_phot3Et_low12.Rebin(4)
h_CR3_phot2Et_low12.Rebin(4)
h_CR3_phot3Et_low12.Rebin(4)
h_CR2_phot3Et_high12.Rebin(4)
h_CR3_phot3Et_high12.Rebin(4)

h_CR1_phot2Et_low12.Divide(h_CR3_phot2Et_low12)
h_CR2_phot3Et_low12.Divide(h_CR3_phot3Et_low12)

h_CR2_phot3Et_high12.Divide(h_CR3_phot3Et_high12)

canva = ROOT.TCanvas("canvas","",200,106,600,600)
canva.Divide(2,1)
canva.cd(1)
h_CR1_phot2Et_low12.Draw("E1")
canva.cd(2)
h_CR2_phot3Et_low12.Draw("E1")

canva.SaveAs("plots/CRfrac_photEt.gif")

h_CR1_phot2Et_low12.SetName("CR1_fraction_phot2ET_low12")
h_CR2_phot3Et_low12.SetName("CR2_fraction_phot3ET_low12")
h_CR2_phot3Et_high12.SetName("CR2_fraction_phot3ET_high12")

fOut = ROOT.TFile("histos/CRfraction.root","RECREATE")
fOut.cd()

h_CR1_phot2Et_low12.Write()
h_CR2_phot3Et_low12.Write()
h_CR2_phot3Et_high12.Write()

fOut.Close()
