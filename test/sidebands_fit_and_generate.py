import ROOT
import tdrstyle, CMS_lumi

#Supress the opening of many Canvas's
ROOT.gROOT.SetBatch(True)   

tdrstyle.setTDRStyle()

M_ggg = ROOT.RooRealVar("M_ggg","Three photon invariant mass",70.,110.,"GeV")

M_ggg.setRange("left",70.,85.)
M_ggg.setRange("right",95.,110.)

a0 = ROOT.RooRealVar("a0","a0",60.,50.,75.)

a1 = ROOT.RooRealVar("a1","a1",0.,-5.,5.)
a2 = ROOT.RooRealVar("a2","a2",0.,-5.,5.)
a3 = ROOT.RooRealVar("a3","a3",0.,-50.,50.)
a4 = ROOT.RooRealVar("a4","a4",0.,-50.,50.)
a5 = ROOT.RooRealVar("a5","a5",0.,-50.,50.)

bkgPDF = ROOT.RooChebychev("bkgPDF","BG function",M_ggg,ROOT.RooArgList(a1,a2))

#bkgPDF = ROOT.RooDstD0BG("bkgPDF","BG function",M_ggg,a0,a1,a2,a3)


_fileIn = ROOT.TFile("histos/ZThreeGamma_data.root")
_treeIn = _fileIn.Get("minitree")

dataset = ROOT.RooDataSet("dataset","dataset",ROOT.RooArgSet(M_ggg),ROOT.RooFit.Import(_treeIn),ROOT.RooFit.Cut("M_ggg < 85. || M_ggg > 95."))

fit_result = bkgPDF.fitTo(dataset,ROOT.RooFit.Range("left,right"),ROOT.RooFit.Save())

print "minNll = ", fit_result.minNll()
print "2Delta_minNll = ", 2*(4305.68735073-fit_result.minNll()) # If 2*(NLL(N)-NLL(N+1)) > 3.85 -> N+1 is significant improvement

xframe = M_ggg.frame(24)
dataset.plotOn(xframe)
bkgPDF.plotOn(xframe)

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
canvas.SaveAs("fit_sideband.pdf")

#data = bkgPDF.generate(ROOT.RooArgSet(M_ggg),388.+295.+329.)
data = ROOT.RooDataSet("data","data",ROOT.RooArgSet(M_ggg),ROOT.RooFit.Import(_treeIn))
data.SetName("data")

ws = ROOT.RooWorkspace("ws_bkg")
getattr(ws,'import')(bkgPDF)
getattr(ws,'import')(data)

_fOut = ROOT.TFile("workspaces/sideband_model.root","RECREATE")
_fOut.cd()
data.Write()
ws.Write()
_fOut.Close()

