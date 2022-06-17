#from DataFormats.FWLite import Events, Handle
import ROOT
import tdrstyle, CMS_lumi

ROOT.gROOT.SetBatch(True)

usedata = False

iPeriod = 4
iPos = 11
CMS_lumi.lumiTextSize = 0.5 #0.9
CMS_lumi.cmsTextSize = 0.5 #1.
CMS_lumi.lumi_13TeV = "137 fb^{-1}"

fNominal = ROOT.TFile("trained/Nominal_training.root")
h_BDT_sig = fNominal.Get("default/Method_BDT/BDT/MVA_BDT_S")
h_BDT_bkg = fNominal.Get("default/Method_BDT/BDT/MVA_BDT_B")
h_BDT_Train_sig = fNominal.Get("default/Method_BDT/BDT/MVA_BDT_Train_S")
h_BDT_Train_bkg = fNominal.Get("default/Method_BDT/BDT/MVA_BDT_Train_B")

fdata = ROOT.TFile("../histos/ZThreeGamma_data.root")
h_BDT_data = fdata.Get("h_BDT_out")

leg1 = ROOT.TLegend(0.65,0.62,0.9,0.87)
leg1.SetHeader("")
leg1.SetFillColor(0)
leg1.SetBorderSize(0)
leg1.SetLineColor(1)
leg1.SetLineStyle(1)
leg1.SetLineWidth(1)
leg1.SetFillStyle(0)
leg1.AddEntry(h_BDT_sig,"Signal","f")
leg1.AddEntry(h_BDT_bkg,"Background","f")

h_BDT_sig.Rebin(2)
h_BDT_bkg.Rebin(2)
h_BDT_Train_sig.Rebin(2)
h_BDT_Train_bkg.Rebin(2)

if usedata :
	h_BDT_data.Rebin(2)
	h_BDT_data.Scale(h_BDT_bkg.Integral()/h_BDT_data.Integral())
	leg1.AddEntry(h_BDT_data,"Data","ep")
	h_BDT_data.SetTitle("")
	h_BDT_data.SetMarkerStyle(20)

ROOT.gStyle.SetErrorX(0.)
ROOT.gStyle.SetOptStat(0)
canvas1 = ROOT.TCanvas()

h_BDT_sig.SetTitle("")
h_BDT_sig.GetXaxis().SetTitle("BDT discriminant")
#h_BDT_sig.GetXaxis().SetTitleSize(0.055)
h_BDT_sig.GetYaxis().SetTitle("Arbitrary units")
#h_BDT_sig.GetYaxis().SetTitleSize(0.055)
h_BDT_sig.SetFillColor(38)
h_BDT_sig.SetFillStyle(3002)

h_BDT_bkg.SetTitle("")
h_BDT_bkg.SetFillColor(2)
h_BDT_bkg.SetLineColor(2)
h_BDT_bkg.SetFillStyle(3002)

h_BDT_Train_sig.SetLineColor(8)
h_BDT_Train_sig.SetMarkerColor(8)
h_BDT_Train_sig.SetMarkerStyle(21)
h_BDT_Train_bkg.SetLineColor(9)
h_BDT_Train_bkg.SetMarkerColor(9)
h_BDT_Train_bkg.SetMarkerStyle(21)

h_BDT_sig.Draw("E1, hist")
h_BDT_bkg.Draw("SAME, E1, hist")
h_BDT_Train_sig.Draw("SAME, lep")
h_BDT_Train_bkg.Draw("SAME, lep")
if usedata :
	h_BDT_data.Draw("SAME, lep")
leg1.Draw("SAME")
CMS_lumi.CMS_lumi(canvas1, iPeriod, iPos)

canvas1.Print("default/BDT_output.pdf")

