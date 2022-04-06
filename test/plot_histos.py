import ROOT
import math
import copy
import sys

#Supress the opening of many Canvas's
ROOT.gROOT.SetBatch(True)   

signal_magnify = 1.
CR_magnify = 1. #2079./1179.

plotOnlyData = True

list_inputfiles = []
#inputnames = ["Signal","data","GJets","ZGToLLG01J","DYJetsToLL","DiPhotonJets",CR1","CR3"]
#inputnames = ["Signal","data","ZGToLLG01J","DYJetsToLL","CR3","GJets","CR2"]
#inputnames = ["Signal","data","CR3","CR1","GGG"]
inputnames = ["Signal","data"]

useSidebands = False
if "SB" in inputnames :
	useSidebands = True

for inputname in inputnames:
	list_inputfiles.append("histos/ZThreeGamma_" + inputname + ".root")

hstack  = dict()
hsignal = dict()
hdata   = dict()
canvas  = dict()
histo_container = [] #just for memory management

#Get the list of histograms
list_histos = []
signalfile = ROOT.TFile("histos/ZThreeGamma_Signal.root")
keylist = signalfile.GetListOfKeys()
key = ROOT.TKey()
for key in keylist :
	obj_class = ROOT.gROOT.GetClass(key.GetClassName())
	if not obj_class.InheritsFrom("TH1") :
		continue
	list_histos.append( key.ReadObj().GetName() )

if not useSidebands :
	for hname in list_histos :
		hstack[hname] = ROOT.THStack("hstack_" + hname,"")

# Color mask
colors_mask = dict()
colors_mask["DYJetsToLL"]   = ROOT.kAzure+7
colors_mask["DiPhotonJets"] = ROOT.kViolet-6
colors_mask["ZGToLLG01J"]   = ROOT.kMagenta+1
colors_mask["CR3"]          = ROOT.kOrange+1
colors_mask["GJets"]        = ROOT.kGreen-7
colors_mask["CR1"]          = ROOT.kBlue-7
colors_mask["CR2"]          = ROOT.kBlue-5
colors_mask["GGG"]          = ROOT.kYellow-8
colors_mask["SB"]           = ROOT.kBlue-7

#Eyecandy
leg1 = ROOT.TLegend(0.6868687,0.6120093,0.9511784,0.9491917) #right positioning
leg1.SetHeader(" ")
leg1.SetFillColor(0)
leg1.SetBorderSize(0)
leg1.SetLineColor(1)
leg1.SetLineStyle(1)
leg1.SetLineWidth(1)
leg1.SetFillStyle(1001)

for filename in list_inputfiles:
	fileIn = ROOT.TFile(filename)

	sample_name = (filename.split("_")[1])[:-5]
	for histo_name in list_histos:
		histo = fileIn.Get(histo_name)

		# Set to 0 the bins containing negative values, due to negative weights
		hsize = histo.GetSize() - 2 # GetSize() returns the number of bins +2 (that is + overflow + underflow) 
		for bin in range(1,hsize+1): # The +1 is in order to get the last bin
			bincontent = histo.GetBinContent(bin)
			if bincontent < 0.:
				histo.SetBinContent(bin,0.)

		histo_container.append(copy.copy(histo))

		if not "h_N" in histo_name :
			histo_container[-1].Rebin(2)

		#if histo_name == "h_threegammass" :
		#	histo_container[-1].Rebin(2)

		if "Signal" in sample_name :
			histo_container[-1].SetLineStyle(2)   #dashed
			histo_container[-1].SetLineColor(2)   #red
			histo_container[-1].SetLineWidth(4)   #kind of thick
			hsignal[histo_name] = histo_container[-1]
		elif "data" in sample_name :
			histo_container[-1].SetMarkerStyle(20)   #point
			hdata[histo_name] = histo_container[-1]
		else :
			histo_container[-1].SetFillColor(colors_mask[sample_name])
			histo_container[-1].SetLineColor(colors_mask[sample_name])
			if not useSidebands :
				hstack[histo_name].Add(histo_container[-1])
			else :
				hstack[histo_name] = histo_container[-1]

		if plotOnlyData :
			hstack[histo_name].Add(histo_container[-1])

		if "threegammas" in histo_name : #Add the legend only once (gammaet is just a random variable)

			if not sample_name == "data" and not sample_name == "Signal":
				leg1.AddEntry(histo_container[-1],sample_name,"f")
			elif sample_name == "data":
				leg1.AddEntry(histo_container[-1],sample_name,"ep")
			elif sample_name == "Signal":
				leg1.AddEntry(histo_container[-1],"Signal (SMx 10^{4})","f")

	fileIn.Close()

for histo_name in list_histos:

	canvas[histo_name] = ROOT.TCanvas("Canvas_" + histo_name,"",200,106,600,600)
	canvas[histo_name].cd()
 
	if not plotOnlyData :	##########################################
		pad1 = ROOT.TPad("pad_" + histo_name,"",0,0.28,1,1.)
		pad2 = ROOT.TPad("pad_" + histo_name,'',0,0.01,1,0.27)
		pad1.SetTopMargin(0.047)
		pad1.SetBottomMargin(0.02)
		pad1.SetBorderMode(0)
		pad1.SetBorderSize(0)
		pad1.SetFrameBorderSize(0)
		pad2.SetBorderSize(0)
		pad2.SetFrameBorderSize(0)
		pad2.SetBottomMargin(0.3)
		pad2.SetBorderMode(0)
		pad1.Draw()
		pad2.Draw()

		pad1.cd()

	hstack[histo_name].SetTitle("")
	hdata[histo_name].SetTitle("")
	hsignal[histo_name].SetTitle("")

	#Manage exclusions
	if "twotrkmass" in histo_name :
		continue

	if signal_magnify != 1:
		hsignal[histo_name].Scale(signal_magnify)      

	if not plotOnlyData :

		if useSidebands :
			hstack[histo_name].Scale(hdata[histo_name].Integral()/hstack[histo_name].Integral())

		hstack[histo_name].Draw("histo")
		hstack[histo_name].GetYaxis().SetTitleSize(0.07)
		hstack[histo_name].GetYaxis().SetTitleOffset(0.7)
		hstack[histo_name].GetYaxis().SetTitle("Events")
		hstack[histo_name].GetXaxis().SetLabelOffset(999)

		if hdata[histo_name].GetMaximum() > hstack[histo_name].GetMaximum() :
			hstack[histo_name].SetMaximum(hdata[histo_name].GetMaximum())

		if hsignal[histo_name].GetMaximum() > hstack[histo_name].GetMaximum() :
			hstack[histo_name].SetMaximum(hsignal[histo_name].GetMaximum())

		if histo_name == "h_m12" :
			#hstack[histo_name].SetMaximum(1000.)
			#hstack[histo_name].Rebin(2)
			hstack[histo_name].GetXaxis().SetTitle("m_{12} (GeV)")

		if histo_name == "h_m13" :
			#hstack[histo_name].SetMaximum(600.)
			hstack[histo_name].GetXaxis().SetTitle("m_{13} (GeV)")

		if histo_name == "h_m23" :
			#hstack[histo_name].SetMaximum(600.)
			hstack[histo_name].GetXaxis().SetTitle("m_{23} (GeV)")

		if histo_name == "h_phot1_ET" :
			#hstack[histo_name].SetMaximum(1200.)
			hstack[histo_name].GetXaxis().SetTitle("E_{T,1} (GeV)")

		if histo_name == "h_phot2_ET" :
			#hstack[histo_name].SetMaximum(1500.)
			hstack[histo_name].GetXaxis().SetTitle("E_{T,2} (GeV)")

		if histo_name == "h_phot3_ET" :
			#hstack[histo_name].SetMaximum(3000.)
			hstack[histo_name].GetXaxis().SetTitle("E_{T,3} (GeV)")

		if histo_name == "h_eta1" :
			hstack[histo_name].GetXaxis().SetTitle("#eta_{1}")

		if histo_name == "h_eta2" :
			hstack[histo_name].GetXaxis().SetTitle("#eta_{2}")

		if histo_name == "h_eta3" :
			#hstack[histo_name].SetMaximum(700.)
			hstack[histo_name].GetXaxis().SetTitle("#eta_{3}")

		if histo_name == "h_threegammass" :
			hstack[histo_name].SetMaximum(300.)
			#hstack[histo_name].Rebin(2)
			#hdata[histo_name].Rebin(2)
			#hsignal[histo_name].Rebin(2)
			hstack[histo_name].GetXaxis().SetTitle("m_{#gamma#gamma#gamma} (GeV)")

		if histo_name == "h_r9_1" :
			hstack[histo_name].GetXaxis().SetTitle("r_{9,1}")

		if histo_name == "h_r9_2" :
			hstack[histo_name].GetXaxis().SetTitle("r_{9,2}")

		if histo_name == "h_r9_3" :
			hstack[histo_name].SetMaximum(2500.)
			hstack[histo_name].GetXaxis().SetTitle("r_{9,3}")

		if histo_name == "h_hoe_1" :
			hstack[histo_name].GetXaxis().SetTitle("(H/E)_{1}")

		if histo_name == "h_hoe_2" :
			hstack[histo_name].GetXaxis().SetTitle("(H/E)_{2}")

		if histo_name == "h_hoe_3" :
			hstack[histo_name].GetXaxis().SetTitle("(H/E)_{3}")

		if histo_name == "h_NPhotons" :
			hstack[histo_name].GetXaxis().SetTitle("N_{#gamma}")

		if "h_NJet" in histo_name :
			hstack[histo_name].GetXaxis().SetTitle("N_{jets}")

		if histo_name == "h_onetrk_pt" :
			hstack[histo_name].GetXaxis().SetTitle("p_{T} (GeV)")

		hstack[histo_name].Draw("SAME,histo")


	if plotOnlyData :
		hdata[histo_name].GetXaxis().SetTitle("m_{#gamma#gamma#gamma} (GeV)")
		hdata[histo_name].SetMaximum(220.)
		hdata[histo_name].Rebin(2)
		hsignal[histo_name].Rebin(2)
		hdata[histo_name].Draw("E1,X0")
		hsignal[histo_name].Draw("SAME,hist")
	else :
		hdata[histo_name].Draw("SAME,E1,X0")
		hsignal[histo_name].Draw("SAME,hist")

	if not useSidebands :
		hMCErr = copy.deepcopy(hstack[histo_name].GetStack().Last())
	else :
		hMCErr = copy.deepcopy(hstack[histo_name])

	hMCErr_size = hMCErr.GetSize() - 2
	hMCErr.SetFillStyle(3005)
	hMCErr.SetMarkerStyle(0)
	hMCErr.SetFillColor(ROOT.kBlack)
	hMCErr.SetLineColor(0)
	if not plotOnlyData :
		hMCErr.Draw("sameE2")

	if "threegamma" in histo_name and not plotOnlyData :#Add the legend only once
		leg1.AddEntry(hMCErr,"Bkg unc","f")
	leg1.Draw()

	################################################

	if not plotOnlyData :
		pad2.cd()
		pad2.SetTopMargin(0.03)
		pad2.SetFillColor(0)
		pad2.SetFillStyle(0)
		ROOT.gStyle.SetOptStat(0)
		totalMC = copy.deepcopy(hMCErr)
		totalData = copy.deepcopy(hdata[histo_name])
		totalData_forErrors = copy.deepcopy(hdata[histo_name])
		totalData.Divide(totalMC)

		for bin in range(1,hMCErr_size+1):
		
			#Set MC error band to MC relative uncertainty
			if not totalMC.GetBinContent(bin) == 0:
				new_MC_BinError = totalMC.GetBinError(bin)/totalMC.GetBinContent(bin)
			else:
				new_MC_BinError = 0.

			#Set data/MC ratio points error bar to data relative uncertainty
			if not totalData_forErrors.GetBinContent(bin) == 0:
				new_Data_BinError = totalData_forErrors.GetBinError(bin)/totalData_forErrors.GetBinContent(bin)
			else:
				new_Data_BinError = 0.

			totalMC.SetBinError(bin,new_MC_BinError)
			totalMC.SetBinContent(bin,1.)
			totalData.SetBinError(bin,new_Data_BinError)
	
		totalData.SetTitle("")
		totalData.SetMarkerStyle(8)
		totalData.SetMarkerColor(1)
		totalData.SetLineColor(1)
		totalData.GetYaxis().SetLabelSize(0.1)
		totalData.GetYaxis().SetTitle("Data/MC")
		totalData.GetYaxis().SetTitleSize(0.16)
		totalData.GetYaxis().SetTitleOffset(0.3)
		totalData.GetYaxis().SetRangeUser(0.,2.)
		totalData.GetYaxis().SetNdivisions(502,ROOT.kFALSE)
		totalData.GetXaxis().SetLabelSize(0.10)
		totalData.GetXaxis().SetTitleSize(0.12)
		totalData.GetXaxis().SetTitleOffset(1.0)
		totalData.GetXaxis().SetTitle(hstack[histo_name].GetXaxis().GetTitle())

		totalMC.SetTitle("")
		totalMC.SetFillStyle(3002)

		line_on_one = ROOT.TLine(totalData.GetXaxis().GetXmin(),1.,totalData.GetXaxis().GetXmax(),1.)
		line_on_one.SetLineColor(4)
		line_on_one.SetLineStyle(2)

		totalData.Draw("E1,X0")
		totalMC.Draw("sameE2")
		line_on_one.Draw("SAME")
	################################################

	canvas[histo_name].SaveAs("plots/" + histo_name + ".pdf")
