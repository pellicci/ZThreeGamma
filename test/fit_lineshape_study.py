	
import ROOT

ROOT.gROOT.ProcessLineSync(".L dCB/RooDoubleCBFast.cc+")

_fSignal = ROOT.TFile("workspaces/signal_model.root")
ws_sig = _fSignal.Get("ws_sig")

_fBkg = ROOT.TFile("workspaces/sideband_model.root")
ws_bkg = _fBkg.Get("ws_bkg")

data = _fBkg.Get("data")

M_ggg = ws_sig.var("M_ggg")

sigPDF = ws_sig.pdf("sigPDF")
bkgPDF = ws_bkg.pdf("bkgPDF")

eff_sig = ROOT.RooRealVar("eff_sig","eff_sig", (484.+ 492. + 1336. + 1051.)/(399.*250. + 200.*500. + 199.*500.))
lumi    = ROOT.RooRealVar("lumi","lumi", 19.52 + 16.81 + 41.48 + 59.83)
cross   = ROOT.RooRealVar("cross","cross", (6225.2/0.0337) * 1000.  )
BRvar   = ROOT.RooRealVar("BRvar","BRvar", 0.0000001,0.,0.000001)
Nsig    = ROOT.RooFormulaVar("Nsig","@0*@1*@2*@3",ROOT.RooArgList(eff_sig,lumi,cross,BRvar))

sigPDF_norm = ROOT.RooFormulaVar("sigPDF_norm","@0*@1*@2",ROOT.RooArgList(eff_sig,lumi,cross))

Nbkg = ROOT.RooRealVar("Nbkg","Nbkg",800.,5.,3000.)

tot_pdf = ROOT.RooAddPdf("tot_pdf","tot_pdf",ROOT.RooArgList(sigPDF,bkgPDF),ROOT.RooArgList(Nsig,Nbkg))

tot_pdf.fitTo(data,ROOT.RooFit.Extended(1))

xframe = M_ggg.frame(18)
data.plotOn(xframe)
tot_pdf.plotOn(xframe)

canvas = ROOT.TCanvas()
canvas.cd()
xframe.Draw()
canvas.SaveAs("fit_alllineshape.pdf")


_fileIn = ROOT.TFile("histos/ZThreeGamma_data.root")
_treeIn = _fileIn.Get("minitree")
data_obs = ROOT.RooDataSet("data_obs","dataset",ROOT.RooArgSet(M_ggg),ROOT.RooFit.Import(_treeIn))

ws = ROOT.RooWorkspace("ws")
getattr(ws,'import')(data_obs)
getattr(ws,'import')(tot_pdf)
getattr(ws,'import')(sigPDF_norm)

_fOut = ROOT.TFile("workspaces/total_model.root","RECREATE")
_fOut.cd()
ws.Write()
_fOut.Close()
