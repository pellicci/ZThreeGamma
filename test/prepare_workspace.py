import ROOT

ROOT.gROOT.SetBatch(True)   

ROOT.gROOT.ProcessLineSync(".L dCB/RooDoubleCBFast.cc+")

_fSignal = ROOT.TFile("workspaces/signal_model.root")
ws_sig = _fSignal.Get("ws_sig")

_fBkg = ROOT.TFile("workspaces/sideband_model.root")
ws_bkg = _fBkg.Get("ws_bkg")

sigPDF = ws_sig.pdf("sigPDF")
bkgPDF = ws_bkg.pdf("bkgPDF")
data = _fBkg.Get("data")

ws = ROOT.RooWorkspace("ws")
getattr(ws,'import')(data)
getattr(ws,'import')(sigPDF)
getattr(ws,'import')(bkgPDF)

_fOut = ROOT.TFile("workspaces/total_model.root","RECREATE")
_fOut.cd()
ws.Write()
_fOut.Close()
