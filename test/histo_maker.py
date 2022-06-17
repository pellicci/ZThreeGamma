#!/usr/bin/env python

import ROOT
import argparse
import math
from array import array
import random

from Workflow_Handler import Workflow_Handler

ROOT.gROOT.SetBatch(True)

do_MVA_Stage = True
cut_MVA = 0.14626722502934086

def select_all_but_one(h_string="NoCut"):

	selection_bools = dict()
	selection_bools["h_NElectrons"] = N_electrons_clean < 1
	selection_bools["h_NPhotons"] = N_photons == 3
	selection_bools["h_r9_1"] = phot1_r9 > 0.9
	selection_bools["h_r9_2"] = phot2_r9 > 0.85
	selection_bools["h_r9_3"] = phot3_r9 > 0.5
	selection_bools["h_met_pt"] = puppiMET_pt < 80.
	selection_bools["h_phot1_ET"] = phot1_pt > 32.
	selection_bools["h_phot2_ET"] = phot2_pt > 20.
	selection_bools["h_phot3_ET"] = phot3_pt > 10.

	result = True

	for hname in selection_bools:
		if h_string == hname:
			continue
		else:
			result = result and selection_bools[hname]
			   
	return result

p = argparse.ArgumentParser(description='Select whether to fill the histograms after pre-selection or selection')
p.add_argument('runningEra_option', help='Type <<0>> for 2016, <<2>> for 2017, <<3>> for 2018')
p.add_argument('CR_option', help='Type <<0>> for SR, >0 for CR')
p.add_argument('SecondPass_option', help='Type <<0>> for first, 1 for second')
p.add_argument('Sidebands_option', help='Type <<0>> for whole spectrum, 1 for inv mass sidebands')
p.add_argument('inputfile_option', help='Provide input file name')
p.add_argument('outputfile_option', help='Provide output file name')
args = p.parse_args()

runningEra = int(args.runningEra_option)
CRflag = int(args.CR_option)
SecondPass = int(args.SecondPass_option)
useSidebands = int(args.Sidebands_option)
input_filename = args.inputfile_option
output_filename = args.outputfile_option

myWF = Workflow_Handler(runningEra)

#Normalize to this luminsity, in fb-1
luminosity_norm = myWF.get_lumi_norm()

# Get the files and the names of the samples
sample_name = input_filename.split("_")[1]

#Understand if this is data or MC
isData = False
if "SingleEG" in sample_name or "DoubleEG" in sample_name :
	isData = True
	print "Analyzing a data sample..."
else :
	print "Analyzing a MC sample..."

if CRflag > 0 or useSidebands :
	print "Processing the control region "
else :
	print "Processing the signal region" 

print "This is the era ", runningEra

if SecondPass and useSidebands :

	print "This is the second pass after weights"
	fileSBfraction = ROOT.TFile("histos/SBfraction.root")
	fileSBfraction.cd()
	histo_SB_phot_fraction  = fileSBfraction.Get("h_data_phot1Et")

#get the MC normalization
Norm_xsec = myWF.get_xsec_norm(sample_name)

#prepare the histos
h_base = dict()

list_histos = ["h_threegammass","h_phot1_ET","h_phot2_ET","h_phot3_ET","h_NElectrons","h_deltaR_Zgam","h_m12","h_m13","h_m23","h_eta1","h_eta2","h_eta3",
	"h_deltaR_12","h_deltaR_13","h_deltaR_23","h_deltaRMin","h_NPhotons","h_NJets","h_NJets_clean","h_twotrkmass","h_onetrk_pt","h_onetrk_eta","h_onetrk_phi",
	"h_met_pt","h_phot4_ET","h_jet_pt","h_r9_1","h_r9_2","h_r9_3","h_hoe_1","h_hoe_2","h_hoe_3","h_Z_pt","h_reliso_1","h_reliso_2","h_reliso_3","h_sumEt","h_sum_gam_ID",
	"h_phot12_ET","h_BDT_out"]

it_h = -1
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "M_{#gamma#gamma#gamma}", 100, 60., 120.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "E_{T,#gamma_{1}}", 60, 20., 110.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "E_{T,#gamma_{2}}", 60, 10., 110.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "E_{T,#gamma_{3}}", 60, 5., 60.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "N_{ele}", 10, -0.5, 9.5)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#Delta R 1,2-3", 30, -1., 10.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "M_{1,2}", 60, 40., 110.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "M_{1,3}", 60, 10., 110.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "M_{2,3}", 60, 10., 110.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#eta_{#gamma_{1}}", 60, -2.6, 2.6)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#eta_{#gamma_{2}}", 60, -2.6, 2.6)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#eta_{#gamma_{3}}", 60, -2.6, 2.6)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#Delta R_{1,2}", 30, -1., 5.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#Delta R_{1,3}", 30, -1., 5.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#Delta R_{2,3}", 30, -1., 5.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#Delta R_{min}", 30, -1., 5.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "N_{#gamma}", 10, -0.5, 9.5)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "N_{jets}", 10, -0.5, 9.5)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "N_{jets} clean", 10, -0.5, 9.5)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "M_{trk,trk}", 30, 0., 120.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "p_{T,trk1}", 60, 0., 120.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#eta_{trk1}}", 60, -5.5, 5.5)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "#phi_{trk1}}", 60, -6.2, 6.2)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "MET", 100, 0., 200.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "E_{T,#gamma_{4}}", 60, 0., 80.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "p_{T,jet}", 60, 0., 120.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "r_{9}", 60, 0.8, 1.1)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "r_{9}", 60, 0.8, 1.1)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "r_{9}", 60, 0.5, 1.1)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "hoe", 60, 0., 0.1)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "hoe", 60, 0., 0.1)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "hoe", 60, 0., 0.3)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "p_{T,Z}", 50, 0., 100.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "Rel Iso", 100, 0., 0.5)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "Rel Iso", 100, 0., 0.5)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "Rel Iso", 100, 0., 0.5)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "Sum ET", 100, 0., 1000.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "Sum of photon ID", 30, 0., 3.1)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH2F(list_histos[it_h], "E_{T,#gamma_{1,2}}", 60, 20., 110.,60,10.,110.)
it_h+=1 ; h_base[list_histos[it_h]] = ROOT.TH1F(list_histos[it_h], "BDT output", 40, -0.51431185, 0.56848429)

##Loop on events
norm_factor = 1.
if not isData:
	norm_factor = Norm_xsec*luminosity_norm
	print "Normalization factor used for ", sample_name, " = ", norm_factor 
	
root_file = ROOT.TFile(input_filename)
mytree = root_file.Get("Events")
print "Processing Sample ", sample_name

Nevts_per_sample   = 0. # Count the number of events in input per each sample processed
Nevts_selected     = 0. # Count the number of events survived per each sample processed
Nevts_expected     = 0. # Number of expected events from weights

nentries = mytree.GetEntriesFast()

#Initializing variables
phot1_FourMom = ROOT.TLorentzVector()
phot2_FourMom = ROOT.TLorentzVector()
phot3_FourMom = ROOT.TLorentzVector()

trk1_FourMom = ROOT.TLorentzVector()
trk2_FourMom = ROOT.TLorentzVector()

##Open the output
fOut = ROOT.TFile(output_filename,"RECREATE")
fOut.cd()

#Variabiles to fill the tree
_phot1_pt      = array('f', [0.])
_phot2_pt      = array('f', [0.])
_phot3_pt      = array('f', [0.])
_phot1_hoe     = array('f', [0.])
_phot2_hoe     = array('f', [0.])
_phot3_hoe     = array('f', [0.])
_phot1_r9      = array('f', [0.])
_phot2_r9      = array('f', [0.])
_phot3_r9      = array('f', [0.])
_phot1_iso     = array('f', [0.])
_phot2_iso     = array('f', [0.])
_phot3_iso     = array('f', [0.])
_met_pt        = array('f', [0.])
_Z_pt          = array('f', [0.])
_m_threeg      = array('f', [0.])
_norm_phot1_pt = array('f', [0.])
_sum_gam_id    = array('f', [0.])
_Event_Weight  = array('f', [0.])

minitree = ROOT.TTree('minitree','tree with branches')

minitree.Branch('Phot1_ET',_phot1_pt,'Phot1_ET/F')
minitree.Branch('Phot2_ET',_phot1_pt,'Phot2_ET/F')
minitree.Branch('Phot3_ET',_phot1_pt,'Phot3_ET/F')
minitree.Branch('Phot1_hoe',_phot1_hoe,'Phot1_hoe/F')
minitree.Branch('Phot2_hoe',_phot2_hoe,'Phot2_hoe/F')
minitree.Branch('Phot3_hoe',_phot3_hoe,'Phot3_hoe/F')
minitree.Branch('Phot1_r9',_phot1_r9,'Phot1_r9/F')
minitree.Branch('Phot2_r9',_phot2_r9,'Phot2_r9/F')
minitree.Branch('Phot3_r9',_phot3_r9,'Phot3_r9/F')
minitree.Branch('Phot1_iso',_phot1_iso,'Phot1_iso/F')
minitree.Branch('Phot2_iso',_phot2_iso,'Phot2_iso/F')
minitree.Branch('Phot3_iso',_phot3_iso,'Phot3_iso/F')
minitree.Branch('MET_pT',_met_pt,'MET_pT/F')
minitree.Branch('Z_pT',_Z_pt,'Z_pT/F')
minitree.Branch('M_ggg',_m_threeg,'M_ggg/F')
minitree.Branch('Sum_gam_id',_sum_gam_id,'Sum_gam_id/F')
minitree.Branch('Event_Weight',_Event_Weight,'Event_Weight/F')

#Prepare the MVA stuff
reader = ROOT.TMVA.Reader("!Color")

reader.AddVariable("Phot1_hoe",_phot1_hoe)
reader.AddVariable("Phot2_hoe",_phot2_hoe)
reader.AddVariable("Phot3_hoe",_phot3_hoe)
reader.AddVariable("Phot1_r9",_phot1_r9)
reader.AddVariable("Phot2_r9",_phot2_r9)
reader.AddVariable("Phot3_r9",_phot3_r9)
reader.AddVariable("Phot1_iso",_phot1_iso)
reader.AddVariable("Phot2_iso",_phot2_iso)
reader.AddVariable("Phot3_iso",_phot3_iso)
reader.AddVariable("MET_pT",_met_pt)
reader.AddVariable("Z_pT",_Z_pt)
reader.AddVariable("Sum_gam_id",_sum_gam_id)

if do_MVA_Stage :
	reader.BookMVA("BDT","MVA/trained/BDT_trained.xml")# First argument is arbitrary. To be chosen in order to distinguish among methods

print "This sample has ", mytree.GetEntriesFast(), " events"

for jentry in xrange(nentries):
	ientry = mytree.LoadTree( jentry )
	if ientry < 0:
		break
	nb = mytree.GetEntry(jentry )
	if nb <= 0:
		continue

	Nevts_per_sample = Nevts_per_sample + 1

	if (Nevts_per_sample/100000.).is_integer() :
		print "Processed ", Nevts_per_sample, " events..."

	#Select based on the control region flag
	#if not mytree.Photon_mvaID_WP80[0] :
	#	continue

	#if CRflag == 0 and not (mytree.Photon_mvaID_WP80[1] and mytree.Photon_mvaID_WP80[2])  :
	#	continue
	#if CRflag == 1 and not (mytree.Photon_mvaID_WP80[1] and not mytree.Photon_mvaID_WP80[2])  :
	#	continue
	#if CRflag == 2 and not (not mytree.Photon_mvaID_WP80[1] and mytree.Photon_mvaID_WP80[2])  :
	#	continue
	#if CRflag == 3 and (mytree.Photon_mvaID_WP80[1] or mytree.Photon_mvaID_WP80[2])  :
	#	continue

	#Get basic variables
	phot1_pt  = mytree.Photon_pt[0]
	phot1_eta = mytree.Photon_eta[0]
	phot1_phi = mytree.Photon_phi[0]
	phot1_r9  = mytree.Photon_r9[0]
	phot1_hoe = mytree.Photon_hoe[0]
	phot1_iso = mytree.Photon_pfRelIso03_all[0]
	phot1_mva = mytree.Photon_mvaID[0]

	phot2_pt  = mytree.Photon_pt[1]
	phot2_eta = mytree.Photon_eta[1]
	phot2_phi = mytree.Photon_phi[1]
	phot2_r9  = mytree.Photon_r9[1]
	phot2_hoe = mytree.Photon_hoe[1]
	phot2_iso = mytree.Photon_pfRelIso03_all[1]
	phot2_mva = mytree.Photon_mvaID[1]

	phot3_pt  = mytree.Photon_pt[2]
	phot3_eta = mytree.Photon_eta[2]
	phot3_phi = mytree.Photon_phi[2]
	phot3_r9  = mytree.Photon_r9[2]
	phot3_hoe = mytree.Photon_hoe[2]
	phot3_iso = mytree.Photon_pfRelIso03_all[2]
	phot3_mva = mytree.Photon_mvaID[2]

	sum_phot_mva = phot1_mva + phot2_mva + phot3_mva

	phot1_FourMom.SetPtEtaPhiM(phot1_pt,phot1_eta,phot1_phi,0.)
	phot2_FourMom.SetPtEtaPhiM(phot2_pt,phot2_eta,phot2_phi,0.)
	phot3_FourMom.SetPtEtaPhiM(phot3_pt,phot3_eta,phot3_phi,0.)

	FourMom_12 = phot1_FourMom + phot2_FourMom
	FourMom_13 = phot1_FourMom + phot3_FourMom
	FourMom_23 = phot2_FourMom + phot3_FourMom
	threephot_FourMom = phot1_FourMom + phot2_FourMom + phot3_FourMom

	Zed_pt = threephot_FourMom.Pt()

	phot4_pt = 0.
	if mytree.nPhoton > 3 :
		phot4_pt = mytree.Photon_pt[3]

	deltaR_Zgam = FourMom_12.DeltaR(phot3_FourMom)
	deltaR_12   = phot1_FourMom.DeltaR(phot2_FourMom)
	deltaR_13   = phot1_FourMom.DeltaR(phot3_FourMom) 
	deltaR_23   = phot2_FourMom.DeltaR(phot3_FourMom)   

	deltaRMin = deltaR_12 if deltaR_12 < deltaR_13 else deltaR_13
	deltaRMin = deltaRMin if deltaRMin < deltaR_23 else deltaR_23

	invmass_12 = FourMom_12.M()
	invmass_13 = FourMom_13.M()
	invmass_23 = FourMom_23.M()

	threephot_invmass = threephot_FourMom.M()

	if threephot_invmass > 120. or threephot_invmass < 65.:
		continue

	#if SecondPass and CRflag == 3 and invmass_12 > 80. :
	#	continue
	#if SecondPass and CRflag == 1 and invmass_12 < 80. :
	#	continue
	#if SecondPass and CRflag == 2 and invmass_12 < 80. :
	#	continue

	#if useSidebands and isData and (threephot_invmass > 86. and threephot_invmass < 94.) :
	if useSidebands and isData and (threephot_invmass > 75. and threephot_invmass < 105.) :
		continue

	twotrk_invmass = -1.
	onetrk_pt = 0.
	onetrk_eta = -5.
	onetrk_phi = -6.
	if mytree.nIsoTrack > 1 :
		trk1_pt  = mytree.IsoTrack_pt[0]
		trk1_eta = mytree.IsoTrack_eta[0]
		trk1_phi = mytree.IsoTrack_phi[0]

		trk2_pt  = mytree.IsoTrack_pt[1]
		trk2_eta = mytree.IsoTrack_eta[1]
		trk2_phi = mytree.IsoTrack_phi[1]

		trk1_FourMom.SetPtEtaPhiM(trk1_pt,trk1_eta,trk1_phi,0.1)
		trk2_FourMom.SetPtEtaPhiM(trk2_pt,trk2_eta,trk2_phi,0.1)

		twotrk_invmass = (trk1_FourMom + trk2_FourMom).M()
	elif mytree.nIsoTrack == 1 :
		onetrk_pt  = mytree.IsoTrack_pt[0]
		onetrk_eta = mytree.IsoTrack_eta[0]
		onetrk_phi = mytree.IsoTrack_phi[0]

	puppiMET_pt    = mytree.PuppiMET_pt
	puppiMET_sumEt = mytree.PuppiMET_sumEt

	#Determine the event weights
	if not isData :
		MC_Weight = mytree.genWeight
		PU_Weight = mytree.puWeight # Add Pile Up weight

		L1prefire_Weight = mytree.L1PreFiringWeight_Nom

		phot1ID_weights , phot1ID_weights_err = myWF.get_photon_scale(phot1_pt,phot1_eta)
		phot2ID_weights , phot2ID_weights_err = myWF.get_photon_scale(phot2_pt,phot2_eta)
		phot3ID_weights , phot3ID_weights_err = myWF.get_photon_scale(phot3_pt,phot3_eta)

		#This is to do systematics, uncomment only in those cases
		#multiplier = 1 if random.random() < 0.5 else -1
		#phot1ID_weights = phot1ID_weights + multiplier * phot1ID_weights_err
		#multiplier = 1 if random.random() < 0.5 else -1
		#phot2ID_weights = phot2ID_weights + multiplier * phot2ID_weights_err
		#multiplier = 1 if random.random() < 0.5 else -1
		#phot3ID_weights = phot3ID_weights + multiplier * phot3ID_weights_err
		
		phot_IDweights = phot1ID_weights * phot2ID_weights * phot3ID_weights

		isBB = False
		if runningEra < 2 and phot1_eta < 1.5 and phot2_eta < 1.5 :
			isBB = True

		phot1_trig_weight , phot1_trig_weight_err = myWF.get_trig_scale(phot1_pt,phot1_eta,phot1_r9,True,isBB) 
		phot2_trig_weight , phot2_trig_weight_err = myWF.get_trig_scale(phot2_pt,phot2_eta,phot2_r9,False,isBB)
		#this part is for systematics
		#phot1_trig_weight = phot1_trig_weight + phot1_trig_weight_err
		#phot2_trig_weight = phot2_trig_weight + phot2_trig_weight_err
		phot_trig_weight = phot1_trig_weight * phot2_trig_weight

		Event_Weight = norm_factor * L1prefire_Weight * phot_IDweights * phot_trig_weight * MC_Weight * PU_Weight/math.fabs(MC_Weight) # Just take the sign of the gen weight
	else :
		Event_Weight = 1.

	if SecondPass and useSidebands:
		#SBweight_phot = histo_SB_phot_fraction.GetBinContent(histo_SB_phot_fraction.FindBin(phot1_pt,phot2_pt))
		SBweight_phot = histo_SB_phot_fraction.GetBinContent(histo_SB_phot_fraction.FindBin(phot1_pt))

		if SBweight_phot > 0. :  
			Event_Weight = Event_Weight * SBweight_phot

	N_electrons_clean = 0.
	for elecount in xrange(mytree.nElectron) :
		if mytree.Electron_pt[elecount] > 5. and mytree.Electron_mvaFall17V2Iso_WPL[elecount] :
			N_electrons_clean += 1.

	N_photons = mytree.nPhoton

	N_jets = mytree.nJet
	N_jets_clean = 0.
	jet_pt = 0.
	for jetcount in xrange(mytree.nJet) :
		if mytree.Jet_jetId[jetcount] > 1. :
			tmp_jet_pt = mytree.Jet_pt[jetcount]
			if mytree.Jet_puId[jetcount] < 6 and tmp_jet_pt < 50. :
				continue
			N_jets_clean += 1.
			if tmp_jet_pt > jet_pt :
				jet_pt = mytree.Jet_pt[jetcount]


	_phot1_pt[0]  = phot1_pt
	_phot2_pt[0]  = phot2_pt
	_phot3_pt[0]  = phot3_pt
	_phot1_hoe[0]     = phot1_hoe
	_phot2_hoe[0]     = phot2_hoe
	_phot3_hoe[0]     = phot3_hoe
	_phot1_r9[0]      = phot1_r9
	_phot2_r9[0]      = phot2_r9
	_phot3_r9[0]      = phot3_r9
	_phot1_iso[0]     = phot1_iso
	_phot2_iso[0]     = phot2_iso
	_phot3_iso[0]     = phot3_iso
	_met_pt[0]        = puppiMET_pt
	_Z_pt[0]          = Zed_pt
	_m_threeg[0]      = threephot_invmass
	_norm_phot1_pt[0] = phot1_pt/threephot_invmass
	_sum_gam_id[0]    = sum_phot_mva
	_Event_Weight[0]  = Event_Weight

	if do_MVA_Stage :
		MVA_val = reader.EvaluateMVA("BDT")
		h_base["h_BDT_out"].Fill(MVA_val,Event_Weight)

		if MVA_val < cut_MVA :
			continue

	if select_all_but_one() :
		h_base["h_deltaR_Zgam"].Fill(deltaR_Zgam,Event_Weight)
		h_base["h_eta1"].Fill(phot1_eta,Event_Weight)
		h_base["h_eta2"].Fill(phot2_eta,Event_Weight)
		h_base["h_eta3"].Fill(phot3_eta,Event_Weight)
		h_base["h_deltaR_12"].Fill(deltaR_12,Event_Weight)
		h_base["h_deltaR_13"].Fill(deltaR_13,Event_Weight)
		h_base["h_deltaR_23"].Fill(deltaR_12,Event_Weight)
		h_base["h_deltaRMin"].Fill(deltaRMin,Event_Weight)
		h_base["h_NJets"].Fill(N_jets,Event_Weight)
		h_base["h_NJets_clean"].Fill(N_jets_clean,Event_Weight)
		h_base["h_twotrkmass"].Fill(twotrk_invmass,Event_Weight)
		h_base["h_onetrk_eta"].Fill(onetrk_eta,Event_Weight)
		h_base["h_onetrk_phi"].Fill(onetrk_phi,Event_Weight)
		h_base["h_jet_pt"].Fill(jet_pt,Event_Weight)
		h_base["h_hoe_1"].Fill(phot1_hoe,Event_Weight)
		h_base["h_hoe_2"].Fill(phot2_hoe,Event_Weight)
		h_base["h_hoe_3"].Fill(phot3_hoe,Event_Weight)
		h_base["h_Z_pt"].Fill(Zed_pt,Event_Weight)
		h_base["h_reliso_1"].Fill(phot1_iso,Event_Weight)
		h_base["h_reliso_2"].Fill(phot2_iso,Event_Weight)
		h_base["h_reliso_3"].Fill(phot3_iso,Event_Weight)
		h_base["h_sumEt"].Fill(puppiMET_sumEt,Event_Weight)
		h_base["h_sum_gam_ID"].Fill(sum_phot_mva,Event_Weight)
		h_base["h_m12"].Fill(invmass_12,Event_Weight)
		h_base["h_m13"].Fill(invmass_13,Event_Weight)
		h_base["h_m23"].Fill(invmass_23,Event_Weight)
		h_base["h_phot12_ET"].Fill(phot1_pt,phot2_pt,Event_Weight)

		if not isData or CRflag > 0 or (isData and (threephot_invmass < 86. or threephot_invmass > 94.)) : 
			h_base["h_threegammass"].Fill(threephot_invmass,Event_Weight)

	if select_all_but_one("h_phot1_ET")   : h_base["h_phot1_ET"].Fill(phot1_pt,Event_Weight)
	if select_all_but_one("h_phot2_ET")   : h_base["h_phot2_ET"].Fill(phot2_pt,Event_Weight)
	if select_all_but_one("h_phot3_ET")   : h_base["h_phot3_ET"].Fill(phot3_pt,Event_Weight)
	if select_all_but_one("h_NElectrons") : h_base["h_NElectrons"].Fill(N_electrons_clean,Event_Weight)
	if select_all_but_one("h_NPhotons")   : h_base["h_NPhotons"].Fill(N_photons,Event_Weight)
	if select_all_but_one("h_NPhotons")   : h_base["h_phot4_ET"].Fill(phot4_pt,Event_Weight)
	if select_all_but_one("h_r9_1")       : h_base["h_r9_1"].Fill(phot1_r9,Event_Weight)
	if select_all_but_one("h_r9_2")       : h_base["h_r9_2"].Fill(phot2_r9,Event_Weight)
	if select_all_but_one("h_r9_3")       : h_base["h_r9_3"].Fill(phot3_r9,Event_Weight)
	if select_all_but_one("h_met_pt")     : h_base["h_met_pt"].Fill(puppiMET_pt,Event_Weight)
	if select_all_but_one("h_onetrk_pt")  : h_base["h_onetrk_pt"].Fill(onetrk_pt,Event_Weight)

	if not select_all_but_one() :
		continue

	minitree.Fill()

	Nevts_selected += 1

	Nevts_expected += Event_Weight # Increment the number of events survived in the analyzed sample

fOut.cd()
for hist_name in list_histos:
	h_base[hist_name].Write()
minitree.Write()
fOut.Close()

print "Number of expected events for ", luminosity_norm, " in fb-1, for sample " , sample_name
print "Number of events processed = ", Nevts_per_sample
print "Number of events selected = ", Nevts_selected
print "Number of events expected = ", Nevts_expected
print "###################"
print "###################"
