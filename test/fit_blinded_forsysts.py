import ROOT

#Supress the opening of many Canvas's
ROOT.gROOT.SetBatch(True)   

ROOT.gROOT.ProcessLineSync(".L dCB/RooDoubleCBFast.cc+")
ROOT.gROOT.ProcessLineSync(".L dCB/RooMultiPdf.cxx+")

_fSignal = ROOT.TFile("workspaces/signal_model.root")
ws_sig = _fSignal.Get("ws_sig")

_fBkg = ROOT.TFile("workspaces/sideband_model.root")
ws_bkg = _fBkg.Get("ws_bkg")

M_ggg = ws_sig.var("M_ggg")

sigPDF = ws_sig.pdf("sigPDF")
bkgPDFcheb = ws_bkg.pdf("bkgPDFcheb")

eff_sig     = ROOT.RooRealVar("eff_sig","eff_sig", (9.24690383365 )/0.0000001)
BRvar       = ROOT.RooRealVar("BRvar","BRvar", 0.0000001,0.,0.000001)
BRvar_blind = ROOT.RooUnblindOffset("BRvar_blind","BRvar_blind","aSeedString",0.0000001,BRvar)
Nsig    = ROOT.RooFormulaVar("Nsig","@0*@1",ROOT.RooArgList(eff_sig,BRvar_blind))

Nbkg = ROOT.RooRealVar("Nbkg","Nbkg",800.,5.,3000.)

tot_pdf = ROOT.RooAddPdf("tot_pdf","tot_pdf",ROOT.RooArgList(sigPDF,bkgPDFcheb),ROOT.RooArgList(Nsig,Nbkg))

_fileIn = ROOT.TFile("histos/ZThreeGamma_data.root")
_treeIn = _fileIn.Get("minitree")
data_obs = ROOT.RooDataSet("data_obs","dataset",ROOT.RooArgSet(M_ggg),ROOT.RooFit.Import(_treeIn))

tot_pdf.fitTo(data_obs,ROOT.RooFit.Extended(1))
