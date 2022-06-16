import ROOT
import tdrstyle, CMS_lumi

#Supress the opening of many Canvas's
ROOT.gROOT.SetBatch(True)   

ROOT.gStyle.SetOptStat(0)
tdrstyle.setTDRStyle()

ROOT.gROOT.ProcessLineSync(".L dCB/RooDoubleCBFast.cc+")

_fSignal = ROOT.TFile("workspaces/signal_model.root")
ws_sig = _fSignal.Get("ws_sig")

_fBkg = ROOT.TFile("workspaces/sideband_model.root")
ws_bkg = _fBkg.Get("ws_bkg")

M_ggg = ws_sig.var("M_ggg")

sigPDF = ws_sig.pdf("sigPDF")
bkgPDF = ws_bkg.pdf("bkgPDF")
sigdataset = ws_sig.data("dataset")

binnedsigdata = sigdataset.binnedClone()
binnedsigPDF = ROOT.RooHistPdf("binnedsigPDF","Binned signal",ROOT.RooArgSet(M_ggg),binnedsigdata)

eff_sig = ROOT.RooRealVar("eff_sig","eff_sig", (58.6922977064 + 50.1889636656 + 122.469802851 + 176.30558011)/( (19.52+16.81+41.48+59.83)*(6404.0*0.000001/0.0337) *1000. ))
lumi    = ROOT.RooRealVar("lumi","lumi", 19.52 + 16.81 + 41.48 + 59.83)
cross   = ROOT.RooRealVar("cross","cross", (6404.0/0.0337) * 1000.  )
BRvar   = ROOT.RooRealVar("BRvar","BRvar", 0.00000001,-0.000001,0.000001)
Nsig    = ROOT.RooFormulaVar("Nsig","@0*@1*@2*@3",ROOT.RooArgList(eff_sig,lumi,cross,BRvar))

Nbkg = ROOT.RooRealVar("Nbkg","Nbkg",2013.,5.,3000.)

tot_pdf = ROOT.RooAddPdf("tot_pdf","tot_pdf",ROOT.RooArgList(sigPDF,bkgPDF),ROOT.RooArgList(Nsig,Nbkg))

#Alternative
#mean_land = ROOT.RooRealVar("mean_land","mean_land",95.574,50.,100.)
#sigma_land = ROOT.RooRealVar("sigma_land","sigma_land",13.8634,0.,40.)
#bkgPDF_land = ROOT.RooLandau("bkgPDF_land","BG function",M_ggg,mean_land,sigma_land)

tot_pdf_alt = ROOT.RooAddPdf("tot_pdf_alt","tot_pdf_alt",ROOT.RooArgList(binnedsigPDF,bkgPDF),ROOT.RooArgList(Nsig,Nbkg))

mc_study = ROOT.RooMCStudy(tot_pdf_alt,ROOT.RooArgSet(M_ggg),ROOT.RooFit.FitModel(tot_pdf),ROOT.RooFit.Extended(1),ROOT.RooFit.FitOptions(ROOT.RooFit.Save(1),ROOT.RooFit.PrintLevel(-1)))

mc_study.generateAndFit(10000)

frame_par = mc_study.plotParam(BRvar, ROOT.RooFit.Bins(40))
frame_err = mc_study.plotError(BRvar, ROOT.RooFit.Bins(40), ROOT.RooFit.FrameRange(0.,30.) )
frame_pul = mc_study.plotPull(BRvar, ROOT.RooFit.Bins(40), ROOT.RooFit.FitGauss(1) )

frame_nll = mc_study.plotNLL(ROOT.RooFit.Bins(40))

mcstudy_Canvas = ROOT.TCanvas("mcstudy_Canvas")
mcstudy_Canvas.Divide(2,2)

mcstudy_Canvas.cd(1)
frame_par.Draw()

mcstudy_Canvas.cd(2)
frame_err.Draw()

mcstudy_Canvas.cd(3)
frame_pul.Draw()

mcstudy_Canvas.cd(4)
frame_nll.Draw()

mcstudy_Canvas.SaveAs("plots/toystudies.png")

