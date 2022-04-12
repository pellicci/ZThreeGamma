	
import ROOT

ROOT.gROOT.ProcessLineSync(".L dCB/RooDoubleCBFast.cc+")

_fSignal = ROOT.TFile("workspaces/signal_model.root")
ws_sig = _fSignal.Get("ws_sig")

_fBkg = ROOT.TFile("workspaces/sideband_model.root")
ws_bkg = _fBkg.Get("ws_bkg")

data = _fBkg.Get("bkg_pdfData")

M_ggg = ws_sig.var("M_ggg")

sig_pdf = ws_sig.pdf("sig_pdf")
bkg_pdf = ws_bkg.pdf("bkg_pdf")

eff_sig = ROOT.RooRealVar("eff_sig","eff_sig", (484.+ 492. + 1336.)/(399.*250. + 200.*500.))
lumi    = ROOT.RooRealVar("lumi","lumi", 19.52 + 16.81 + 41.48)
cross   = ROOT.RooRealVar("cross","cross", (6225.2/0.0337) * 1000.  )
BRvar   = ROOT.RooRealVar("BRvar","BRvar", 0.0000001,0.,0.000001)
Nsig    = ROOT.RooFormulaVar("Nsig","@0*@1*@2*@3",ROOT.RooArgList(eff_sig,lumi,cross,BRvar))

Nbkg = ROOT.RooRealVar("Nbkg","Nbkg",800.,5.,3000.)

tot_pdf = ROOT.RooAddPdf("tot_pdf","tot_pdf",ROOT.RooArgList(sig_pdf,bkg_pdf),ROOT.RooArgList(Nsig,Nbkg))

tot_pdf.fitTo(data,ROOT.RooFit.Extended(1))

xframe = M_ggg.frame(18)
data.plotOn(xframe)
tot_pdf.plotOn(xframe)

canvas = ROOT.TCanvas()
canvas.cd()
xframe.Draw()
canvas.SaveAs("fit_alllineshape.pdf")

ws = ROOT.RooWorkspace("ws")
getattr(ws,'import')(data)
getattr(ws,'import')(tot_pdf)

_fOut = ROOT.TFile("workspaces/total_model.root","RECREATE")
_fOut.cd()
ws.Write()
_fOut.Close()
