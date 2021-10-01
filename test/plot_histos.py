import copy
import ROOT

#open the input files
filelist_2016 = dict()

filelist_2016["Signal"]       = ROOT.TFile("histos/ZThreeGamma_Signal.root")
filelist_2016["DYJetsToLL"]   = ROOT.TFile("histos/ZThreeGamma_DYJetsToLL.root")
filelist_2016["DiPhotonJets"] = ROOT.TFile("histos/ZThreeGamma_DiPhotonJets.root")
filelist_2016["ZGToLLG_01J"]  = ROOT.TFile("histos/ZThreeGamma_ZGToLLG_01J.root")

colors_mask = dict()
colors_mask["DYJetsToLL"]         = ROOT.kAzure+7
colors_mask["DiPhotonJets"]       = ROOT.kViolet-6
colors_mask["ZGToLLG_01J"]        = ROOT.kMagenta+1

#Get the list of histograms
histo_list = []
keylist = (list(filelist_2016.values())[0]).GetListOfKeys()
key = ROOT.TKey()
for key in keylist :
	obj_class = ROOT.gROOT.GetClass(key.GetClassName())
	if not obj_class.InheritsFrom("TH1") :
		continue
	histo_list.append( key.ReadObj().GetName() )

hstack = dict()
hsignal = dict()
for histo_key in histo_list :
    hstack[histo_key] = ROOT.THStack("hstack_" + histo_key,"")

#Eyecandy
leg1 = ROOT.TLegend(0.6868687,0.6120093,0.9511784,0.9491917) #right positioning
leg1.SetHeader(" ")
leg1.SetFillColor(0)
leg1.SetBorderSize(0)
leg1.SetLineColor(1)
leg1.SetLineStyle(1)
leg1.SetLineWidth(1)
leg1.SetFillStyle(1001)

for fileobj in filelist_2016 :
	if fileobj == "Signal" :
		continue
	for histo_key in hstack :

		#for memory management
		print histo_key
		histo_container = copy.copy(filelist_2016[fileobj].Get(histo_key))

		histo_container.SetFillColor(colors_mask[fileobj])

		histo_container.Rebin(2)

		hstack[histo_key].Add(histo_container)

		if histo_key == "h_threegammass" :
			leg1.AddEntry(histo_container, fileobj,"f")

for histo_key in histo_list :
	histo_container = copy.copy(filelist_2016["Signal"].Get(histo_key))
	histo_container.Rebin(2)
	histo_container.SetLineStyle(2)   #dashed
	histo_container.SetLineWidth(4)   #kind of thick

	hsignal[histo_key] = histo_container

	if histo_key == "h_threegammass" :
			leg1.AddEntry(histo_container,"Signal","f")



for histo_key in histo_list :
	canvas = ROOT.TCanvas("Cavas_" + histo_key,"",200,106,600,600)
	canvas.cd()
	hstack[histo_key].SetTitle("")
	hstack[histo_key].Draw("histo")
	hsignal[histo_key].Draw("SAME,hist")
	leg1.Draw()
	canvas.SaveAs("plots/" + histo_key + ".gif")

