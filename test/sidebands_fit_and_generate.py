import ROOT

M_ggg = ROOT.RooRealVar("M_ggg","Three photon invariant mass",70.,110.,"GeV")

M_ggg.setRange("left",70.,85.)
M_ggg.setRange("right",95.,110.)


a0 = ROOT.RooRealVar("a0","a0",70.,60.,80.)

a1 = ROOT.RooRealVar("a1","a1",0.,-5.,5.)
a2 = ROOT.RooRealVar("a2","a2",0.,-5.,5.)
a3 = ROOT.RooRealVar("a3","a3",0.,-50.,50.)
a4 = ROOT.RooRealVar("a4","a4",0.,-50.,50.)
a5 = ROOT.RooRealVar("a5","a5",0.,-50.,50.)

bkgPDF = ROOT.RooChebychev("bkgPDF","BG function",M_ggg,ROOT.RooArgList(a1,a2))

#bkgPDF = ROOT.RooDstD0BG("bkgPDF","BG function",M_ggg,a0,a1,a2,a3)


_fileIn = ROOT.TFile("histos/ZThreeGamma_SB.root")
_treeIn = _fileIn.Get("minitree")

dataset = ROOT.RooDataSet("dataset","dataset",ROOT.RooArgSet(M_ggg),ROOT.RooFit.Import(_treeIn))

bkgPDF.fitTo(dataset,ROOT.RooFit.Range("left,right"))


xframe = M_ggg.frame(24)
dataset.plotOn(xframe)
bkgPDF.plotOn(xframe)

canvas = ROOT.TCanvas()
canvas.cd()
xframe.Draw()
canvas.SaveAs("fit_sideband.pdf")

data = bkgPDF.generate(ROOT.RooArgSet(M_ggg),388.+295.+329.)
data.SetName("data")

ws = ROOT.RooWorkspace("ws_bkg")
getattr(ws,'import')(bkgPDF)
getattr(ws,'import')(data)

_fOut = ROOT.TFile("workspaces/sideband_model.root","RECREATE")
_fOut.cd()
data.Write()
ws.Write()
_fOut.Close()

