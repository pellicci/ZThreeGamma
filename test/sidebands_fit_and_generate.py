import ROOT
import tdrstyle, CMS_lumi

#Supress the opening of many Canvas's
ROOT.gROOT.SetBatch(True)   

tdrstyle.setTDRStyle()

ROOT.gROOT.ProcessLineSync(".L dCB/RooMultiPdf.cxx+")

M_ggg = ROOT.RooRealVar("M_ggg","Three photon invariant mass",70.,110.,"GeV")

M_ggg.setRange("left",70.,85.)
M_ggg.setRange("right",95.,110.)

a0 = ROOT.RooRealVar("a0","a0",60.,50.,75.)

a1 = ROOT.RooRealVar("a1","a1",0.,-5.,5.)
a2 = ROOT.RooRealVar("a2","a2",0.,-5.,5.)
a3 = ROOT.RooRealVar("a3","a3",0.,-50.,50.)
a4 = ROOT.RooRealVar("a4","a4",0.,-50.,50.)
a5 = ROOT.RooRealVar("a5","a5",0.,-50.,50.)
bkgPDFcheb = ROOT.RooChebychev("bkgPDFcheb","BG function",M_ggg,ROOT.RooArgList(a1,a2))

mean_land = ROOT.RooRealVar("mean_land","mean_land",90.,50.,120.)
sigma_land = ROOT.RooRealVar("sigma_land","sigma_land",10.,0.,40.)
bkgPDFland = ROOT.RooLandau("bkgPDFland","BG function",M_ggg,mean_land,sigma_land)

_fileIn = ROOT.TFile("histos/ZThreeGamma_data.root")
_treeIn = _fileIn.Get("minitree")

###Blind, only fit sidebands
dataset = ROOT.RooDataSet("dataset","dataset",ROOT.RooArgSet(M_ggg),ROOT.RooFit.Import(_treeIn),ROOT.RooFit.Cut("M_ggg < 85. || M_ggg > 95."))

fit_result1 = bkgPDFcheb.fitTo(dataset,ROOT.RooFit.Range("left,right"),ROOT.RooFit.Save())
fit_result2 = bkgPDFland.fitTo(dataset,ROOT.RooFit.Range("left,right"),ROOT.RooFit.Save())

print "minNll = ", fit_result1.minNll()
print "2Delta_minNll = ", 2*(4305.68735073-fit_result1.minNll()) # If 2*(NLL(N)-NLL(N+1)) > 3.85 -> N+1 is significant improvement

xframe = M_ggg.frame(24)
dataset.plotOn(xframe)
bkgPDFcheb.plotOn(xframe)

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
canvas.SaveAs("plots/fit_sideband.pdf")

data_obs = bkgPDFcheb.generate(ROOT.RooArgSet(M_ggg), 1455)
data_obs.SetName("data_obs")

cat = ROOT.RooCategory("pdf_index","Index of Pdf which is active")
mypdfs = ROOT.RooArgList()
mypdfs.add(bkgPDFcheb)
mypdfs.add(bkgPDFland)

multipdf = ROOT.RooMultiPdf("multipdf","All Pdfs",cat,mypdfs)

ws = ROOT.RooWorkspace("ws_bkg")
getattr(ws,'import')(data_obs)
#getattr(ws,'import')(cat)
#getattr(ws,'import')(multipdf)
getattr(ws,'import')(bkgPDFland)
getattr(ws,'import')(bkgPDFcheb)

_fOut = ROOT.TFile("workspaces/sideband_model.root","RECREATE")
_fOut.cd()
data_obs.Write()
ws.Write()
_fOut.Close()
