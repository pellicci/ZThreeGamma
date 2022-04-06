
import ROOT

ROOT.gROOT.ProcessLineSync(".L dCB/RooDoubleCBFast.cc+")

M_ggg = ROOT.RooRealVar("M_ggg","Three photon invariant mass",70.,110.,"GeV")

_fileIn = ROOT.TFile("histos/ZThreeGamma_Signal.root")
_treeIn = _fileIn.Get("minitree")

dataset = ROOT.RooDataSet("dataset","dataset",ROOT.RooArgSet(M_ggg),ROOT.RooFit.Import(_treeIn))

m0 = ROOT.RooRealVar("m0","m0",91.,85.,95.)
sigma   = ROOT.RooRealVar("sigma","sigma",2.,0.1,5.)
alpha_L = ROOT.RooRealVar("alpha_L","alpha_L",1.,0.,10.)
alpha_R = ROOT.RooRealVar("alpha_R","alpha_R",1.,0.,10.)
enne_L  = ROOT.RooRealVar("enne_L","enne_L",10.)#,0.1,100.)
enne_R  = ROOT.RooRealVar("enne_R","enne_R",1.,0.1,100.)

sig_pdf = ROOT.RooDoubleCBFast("sig_pdf", "Double Crystal Ball", M_ggg, m0, sigma, alpha_L, enne_L, alpha_R, enne_R)

sig_pdf.fitTo(dataset)

xframe = M_ggg.frame(25)
dataset.plotOn(xframe)
sig_pdf.plotOn(xframe)

canvas = ROOT.TCanvas()
canvas.cd()
xframe.Draw()
canvas.SaveAs("fit_signal.pdf")

m0.setConstant(1)
sigma.setConstant(1)
alpha_L.setConstant(1)
alpha_R.setConstant(1)
enne_L.setConstant(1)
enne_R.setConstant(1)

ws = ROOT.RooWorkspace("ws_sig")
getattr(ws,'import')(sig_pdf)

_fOut = ROOT.TFile("workspaces/signal_model.root","RECREATE")
_fOut.cd()
ws.Write()
_fOut.Close()

