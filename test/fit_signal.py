
import ROOT
import tdrstyle, CMS_lumi

#Supress the opening of many Canvas's
ROOT.gROOT.SetBatch(True)   

tdrstyle.setTDRStyle()

ROOT.gROOT.ProcessLineSync(".L dCB/RooDoubleCBFast.cc+")

M_ggg        = ROOT.RooRealVar("M_ggg","Three photon invariant mass",70.,110.,"GeV")
Event_Weight = ROOT.RooRealVar("Event_Weight","Event Weight",-100.,100.,"GeV")

_fileIn = ROOT.TFile("histos/ZThreeGamma_Signal.root")
_treeIn = _fileIn.Get("minitree")

dataset = ROOT.RooDataSet("dataset","dataset",ROOT.RooArgSet(M_ggg,Event_Weight),ROOT.RooFit.Import(_treeIn),ROOT.RooFit.WeightVar("Event_Weight"))

m0 = ROOT.RooRealVar("m0","m0",91.,85.,95.)
sigma   = ROOT.RooRealVar("sigma","sigma",2.,0.1,5.)
alpha_L = ROOT.RooRealVar("alpha_L","alpha_L",1.,0.,10.)
alpha_R = ROOT.RooRealVar("alpha_R","alpha_R",1.,0.,10.)
enne_L  = ROOT.RooRealVar("enne_L","enne_L",10.,0.1,100.)
enne_R  = ROOT.RooRealVar("enne_R","enne_R",10.,0.1,100.)

sigPDF = ROOT.RooDoubleCBFast("sigPDF", "Double Crystal Ball", M_ggg, m0, sigma, alpha_L, enne_L, alpha_R, enne_R)

sigPDF.fitTo(dataset)

xframe = M_ggg.frame(25)
dataset.plotOn(xframe)
sigPDF.plotOn(xframe)

pullHist = xframe.pullHist()
framePull = M_ggg.frame(25)
framePull.addPlotable(pullHist,"P")
framePull.SetMinimum(-5.)
framePull.SetMaximum(5.)
framePull.SetXTitle("")

canvas = ROOT.TCanvas()
canvas.cd()
pad3 = ROOT.TPad("pad3","pad3",0.01,0.20,0.99,0.99)
pad4 = ROOT.TPad("pad4","pad4",0.01,0.01,0.99,0.20)
pad3.Draw()
pad4.Draw()

pad3.cd()
xframe.Draw()

pad4.cd()
framePull.Draw()
canvas.Update()
canvas.SaveAs("plots/fit_signal.pdf")

m0.setConstant(1)
sigma.setConstant(1)
alpha_L.setConstant(1)
alpha_R.setConstant(1)
enne_L.setConstant(1)
enne_R.setConstant(1)

ws = ROOT.RooWorkspace("ws_sig")
getattr(ws,'import')(sigPDF)
getattr(ws,'import')(dataset)

_fOut = ROOT.TFile("workspaces/signal_model.root","RECREATE")
_fOut.cd()
ws.Write()
_fOut.Close()

