#!/usr/bin/env python

import ROOT
import argparse
import math

def get_xsec_norm(runningEra, sample_name) :
	if runningEra == 0 :
		if "Signal" in sample_name : return float( (6225.2*0.000001/0.0337) *1000./ (199.*250.))
        if "DiPhotonJets" in sample_name : return float( 126.2 *1000./ (2359151. *(1.-2.*0.2363)))
        if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (91988603. *(1.-2.*0.1643) + 95237235.*(1.-2.*0.1643)) )
        if "ZGToLLG" in sample_name : return float( 51.1 *1000./ (27805647.*(1.-2.*0.1923) + 31606911.*(1-2.*0.1923) ))
        if "GJets40To100" in sample_name : return float( 18540. *1000./ (8952278. + 9082742. ))
        if "GJets100To200" in sample_name : return float( 8644. *1000./ (9332192. + 9882256. ))
        if "GJets200To400" in sample_name : return float( 2183. *1000./ (19087322. + 19874909. ))
        if "GJets400To600" in sample_name : return float( 260.2 *1000./ (4242991. + 4629781. ))
        if "GJets600ToInf" in sample_name : return float( 86.58 *1000./ (4661194. + 4366096. ))

	return 1.

def select_all_but_one(h_string="NoCut"):

    selection_bools = dict()
    selection_bools["h_nElectrons"] = N_electrons_clean < 2
    selection_bools["h_m12"] = invmass_12 < 100. #80.
    selection_bools["h_m13"] = invmass_13 < 100. #70.
    selection_bools["h_m23"] = invmass_23 < 100. #70.

    result = True

    for hname in selection_bools:
        if h_string == hname:
            continue
        else:
            result = result and selection_bools[hname]
               
    return result

p = argparse.ArgumentParser(description='Select whether to fill the histograms after pre-selection or selection')
p.add_argument('runningEra_option', help='Type <<0>> for 2016, <<1>> for 2017, <<2>> for 2018, <<3>> for combination of years')
p.add_argument('CR_option', help='Type <<0>> for SR, >0 for CR')
p.add_argument('SecondPass_option', help='Type <<0>> for first, 1 for second')
p.add_argument('inputfile_option', help='Provide input file name')
p.add_argument('outputfile_option', help='Provide output file name')
args = p.parse_args()

runningEra = int(args.runningEra_option)
CRflag = int(args.CR_option)
SecondPass = int(args.SecondPass_option)
input_filename = args.inputfile_option
output_filename = args.outputfile_option

#Normalize to this luminsity, in fb-1
luminosity_norm = 1.
if runningEra == 0 :
    luminosity_norm = 35.92

# Get the files and the names of the samples
sample_name = input_filename.split("_")[1]

#Understand if this is data or MC
isData = False
if "SingleEG" in sample_name or "DoubleEG" in sample_name :
    isData = True
    print "Analyzing a data sample..."
else :
	print "Analyzing a MC sample..."

if CRflag > 0 :
    print "Processing the control region ", CRflag
else :
    print "Processing the signal region"

if SecondPass and not CRflag == 0 :
    fileCRfraction = ROOT.TFile("histos/CRfraction.root")
    fileCRfraction.cd()
    histo_CR1_phot2_low12_fraction  = fileCRfraction.Get("CR1_fraction_phot2ET_low12")
    histo_CR2_phot3_low12_fraction  = fileCRfraction.Get("CR2_fraction_phot3ET_low12")
    histo_CR2_phot3_high12_fraction = fileCRfraction.Get("CR2_fraction_phot3ET_high12")

#get the MC normalization
Norm_xsec = get_xsec_norm(runningEra, sample_name)

#prepare the histos
h_base = dict()

list_histos = ["h_threegammass","h_phot1_ET","h_phot2_ET","h_phot3_ET","h_nElectrons","h_deltaR_Zgam","h_m12","h_m13","h_m23","h_eta1","h_eta2","h_eta3","h_eta1_invmass",
    "h_eta2_invmass","h_deltaR_12","h_deltaR_13","h_deltaR_23","h_deltaRMin","h_NPhotons","h_NJets","h_NJets_clean","h_twotrkmass","h_onetrk_pt","h_onetrk_eta","h_onetrk_phi",
    "h_met_pt","h_phot4_ET","h_jet_pt","h_r9_1","h_r9_2","h_r9_3","h_hoe_1","h_hoe_2","h_hoe_3","h_phot2_ET_low12","h_phot3_ET_low12","h_phot2_ET_high12","h_phot3_ET_high12"]

h_base[list_histos[0]] = ROOT.TH1F(list_histos[0], "M_{#gamma#gamma#gamma}", 60, 60., 120.)
h_base[list_histos[1]] = ROOT.TH1F(list_histos[1], "E_{T,#gamma_{1}}", 60, 20., 120.)
h_base[list_histos[2]] = ROOT.TH1F(list_histos[2], "E_{T,#gamma_{2}}", 60, 10., 120.)
h_base[list_histos[3]] = ROOT.TH1F(list_histos[3], "E_{T,#gamma_{3}}", 60, 5., 80.)
h_base[list_histos[4]] = ROOT.TH1F(list_histos[4], "N_{ele}", 10, -0.5, 9.5)
h_base[list_histos[5]] = ROOT.TH1F(list_histos[5], "#Delta R 1,2-3", 30, -1., 10.)
h_base[list_histos[6]] = ROOT.TH1F(list_histos[6], "M_{1,2}", 60, 40., 100.)
h_base[list_histos[7]] = ROOT.TH1F(list_histos[7], "M_{1,3}", 60, 20., 100.)
h_base[list_histos[8]] = ROOT.TH1F(list_histos[8], "M_{2,3}", 60, 20., 100.)
h_base[list_histos[9]] = ROOT.TH1F(list_histos[9], "#eta_{#gamma_{1}}", 60, -3.5, 3.5)
h_base[list_histos[10]] = ROOT.TH1F(list_histos[10], "#eta_{#gamma_{2}}", 60, -3.5, 3.5)
h_base[list_histos[11]] = ROOT.TH1F(list_histos[11], "#eta_{#gamma_{3}}", 60, -3.5, 3.5)
h_base[list_histos[12]] = ROOT.TH1F(list_histos[12], "#eta_{#gamma_{1}}", 60, -3.5, 3.5)
h_base[list_histos[13]] = ROOT.TH1F(list_histos[13], "#eta_{#gamma_{1}}", 60, -3.5, 3.5)
h_base[list_histos[14]] = ROOT.TH1F(list_histos[14], "#Delta R_{1,2}", 30, -1., 5.)
h_base[list_histos[15]] = ROOT.TH1F(list_histos[15], "#Delta R_{1,3}", 30, -1., 5.)
h_base[list_histos[16]] = ROOT.TH1F(list_histos[16], "#Delta R_{2,3}", 30, -1., 5.)
h_base[list_histos[17]] = ROOT.TH1F(list_histos[17], "#Delta R_{min}", 30, -1., 5.)
h_base[list_histos[18]] = ROOT.TH1F(list_histos[18], "N_{#gamma}", 10, -0.5, 9.5)
h_base[list_histos[19]] = ROOT.TH1F(list_histos[19], "N_{jets}", 10, -0.5, 9.5)
h_base[list_histos[20]] = ROOT.TH1F(list_histos[20], "N_{jets} clean", 10, -0.5, 9.5)
h_base[list_histos[21]] = ROOT.TH1F(list_histos[21], "M_{trk,trk}", 30, 0., 120.)
h_base[list_histos[22]] = ROOT.TH1F(list_histos[22], "p_{T,trk1}", 60, 0., 120.)
h_base[list_histos[23]] = ROOT.TH1F(list_histos[23], "#eta_{trk1}}", 60, -5.5, 5.5)
h_base[list_histos[24]] = ROOT.TH1F(list_histos[24], "#phi_{trk1}}", 60, -6.2, 6.2)
h_base[list_histos[25]] = ROOT.TH1F(list_histos[25], "MET", 100, 0., 200.)
h_base[list_histos[26]] = ROOT.TH1F(list_histos[26], "E_{T,#gamma_{4}}", 60, 0., 80.)
h_base[list_histos[27]] = ROOT.TH1F(list_histos[27], "p_{T,jet}", 60, 0., 120.)
h_base[list_histos[28]] = ROOT.TH1F(list_histos[28], "r_{9}", 60, 0.8, 1.1)
h_base[list_histos[29]] = ROOT.TH1F(list_histos[29], "r_{9}", 60, 0.8, 1.1)
h_base[list_histos[30]] = ROOT.TH1F(list_histos[30], "r_{9}", 60, 0.5, 1.1)
h_base[list_histos[31]] = ROOT.TH1F(list_histos[31], "hoe", 60, 0., 0.1)
h_base[list_histos[32]] = ROOT.TH1F(list_histos[32], "hoe", 60, 0., 0.1)
h_base[list_histos[33]] = ROOT.TH1F(list_histos[33], "hoe", 60, 0., 0.3)
h_base[list_histos[34]] = ROOT.TH1F(list_histos[34], "E_{T,#gamma_{2}}", 60, 10., 120.)
h_base[list_histos[35]] = ROOT.TH1F(list_histos[35], "E_{T,#gamma_{3}}", 60, 5., 80.)
h_base[list_histos[36]] = ROOT.TH1F(list_histos[36], "E_{T,#gamma_{2}}", 60, 10., 120.)
h_base[list_histos[37]] = ROOT.TH1F(list_histos[37], "E_{T,#gamma_{3}}", 60, 5., 80.)

##Open the output
fOut = ROOT.TFile(output_filename,"RECREATE")
fOut.cd()

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
    if CRflag == 0 and not (mytree.Photon_mvaID_WP80[1] and mytree.Photon_mvaID_WP80[2])  :
        continue

    if CRflag == 1 and not (mytree.Photon_mvaID_WP80[1] and not mytree.Photon_mvaID_WP80[2])  :
        continue

    if CRflag == 2 and not (not mytree.Photon_mvaID_WP80[1] and mytree.Photon_mvaID_WP80[2])  :
        continue

    if CRflag == 3 and (mytree.Photon_mvaID_WP80[1] or mytree.Photon_mvaID_WP80[2])  :
        continue

    if not (mytree.Photon_electronVeto[0] and mytree.Photon_electronVeto[1] and mytree.Photon_electronVeto[2]) :
        continue

    #Get basic variables
    phot1_pt  = mytree.Photon_pt[0]
    phot1_eta = mytree.Photon_eta[0]
    phot1_phi = mytree.Photon_phi[0]
    phot1_r9  = mytree.Photon_r9[0]
    phot1_hoe = mytree.Photon_hoe[0]

    phot2_pt  = mytree.Photon_pt[1]
    phot2_eta = mytree.Photon_eta[1]
    phot2_phi = mytree.Photon_phi[1]
    phot2_r9  = mytree.Photon_r9[1]
    phot2_hoe = mytree.Photon_hoe[1]

    phot3_pt  = mytree.Photon_pt[2]
    phot3_eta = mytree.Photon_eta[2]
    phot3_phi = mytree.Photon_phi[2]
    phot3_r9  = mytree.Photon_r9[2]
    phot3_hoe = mytree.Photon_hoe[2]

    #trigger offline preselection
    isEBphot1 = True if abs(phot1_eta) < 1.48 else False
    isEBphot2 = True if abs(phot2_eta) < 1.48 else False

    if phot1_hoe > 0.1 or phot2_hoe > 0.1 :
        continue
    if (isEBphot1 and phot1_r9 < 0.85) or (not isEBphot1 and phot1_r9 < 0.9) :
        continue
    if (isEBphot2 and phot2_r9 < 0.85) or (not isEBphot2 and phot2_r9 < 0.9) :
        continue
    if abs(phot2_eta) > 2.5 :
        continue
    if (isEBphot1 and mytree.Photon_sieie[0] > 0.015) or (not isEBphot1 and mytree.Photon_sieie[0] > 0.035) :
        continue
    if (isEBphot2 and mytree.Photon_sieie[1] > 0.015) or (not isEBphot2 and mytree.Photon_sieie[1] > 0.035) :
        continue

    phot1_FourMom.SetPtEtaPhiM(phot1_pt,phot1_eta,phot1_phi,0.)
    phot2_FourMom.SetPtEtaPhiM(phot2_pt,phot2_eta,phot2_phi,0.)
    phot3_FourMom.SetPtEtaPhiM(phot3_pt,phot3_eta,phot3_phi,0.)

    FourMom_12 = phot1_FourMom + phot2_FourMom
    FourMom_13 = phot1_FourMom + phot3_FourMom
    FourMom_23 = phot2_FourMom + phot3_FourMom
    threephot_FourMom = phot1_FourMom + phot2_FourMom + phot3_FourMom

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

    if SecondPass and CRflag == 3 and invmass_12 > 80. :
        continue
    if SecondPass and CRflag == 1 and invmass_12 < 80. :
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

    puppiMET_pt = mytree.PuppiMET_pt

    #Determine the event weights
    if not isData :
    	MC_Weight = mytree.genWeight
        PU_Weight = mytree.puWeight # Add Pile Up weight

        Event_Weight = norm_factor*MC_Weight*PU_Weight/math.fabs(MC_Weight) # Just take the sign of the gen weight
    else :
    	Event_Weight = 1.

    if CRflag == 3 and SecondPass :
        CRweight_phot2 = histo_CR1_phot2_low12_fraction.GetBinContent(histo_CR1_phot2_low12_fraction.FindBin(phot2_pt))
        CRweight_phot3 = histo_CR2_phot3_low12_fraction.GetBinContent(histo_CR2_phot3_low12_fraction.FindBin(phot3_pt))
        CRweight = CRweight_phot2*CRweight_phot3
        if CRweight > 0. :  
            Event_Weight = Event_Weight * CRweight 

    if CRflag == 1 and SecondPass :
        CRweight = histo_CR2_phot3_high12_fraction.GetBinContent(histo_CR2_phot3_high12_fraction.FindBin(phot3_pt))
        if CRweight > 0. :  
            Event_Weight = Event_Weight * CRweight 

    N_electrons_clean = 0.
    for elecount in xrange(mytree.nElectron) :
        if mytree.Electron_pt[elecount] > 5. :
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

    if select_all_but_one() :
        h_base["h_phot1_ET"].Fill(phot1_pt,Event_Weight)
        h_base["h_phot2_ET"].Fill(phot2_pt,Event_Weight)
        h_base["h_phot3_ET"].Fill(phot3_pt,Event_Weight)
        h_base["h_phot4_ET"].Fill(phot4_pt,Event_Weight)
        h_base["h_deltaR_Zgam"].Fill(deltaR_Zgam,Event_Weight)
        h_base["h_eta1"].Fill(phot1_eta,Event_Weight)
        h_base["h_eta2"].Fill(phot2_eta,Event_Weight)
        h_base["h_eta3"].Fill(phot3_eta,Event_Weight)
        h_base["h_deltaR_12"].Fill(deltaR_12,Event_Weight)
        h_base["h_deltaR_13"].Fill(deltaR_13,Event_Weight)
        h_base["h_deltaR_23"].Fill(deltaR_12,Event_Weight)
        h_base["h_deltaRMin"].Fill(deltaRMin,Event_Weight)
        h_base["h_NPhotons"].Fill(N_photons,Event_Weight)
        h_base["h_NJets"].Fill(N_jets,Event_Weight)
        h_base["h_NJets_clean"].Fill(N_jets_clean,Event_Weight)
        h_base["h_twotrkmass"].Fill(twotrk_invmass,Event_Weight)
        h_base["h_onetrk_pt"].Fill(onetrk_pt,Event_Weight)
        h_base["h_onetrk_eta"].Fill(onetrk_eta,Event_Weight)
        h_base["h_onetrk_phi"].Fill(onetrk_phi,Event_Weight)
        h_base["h_met_pt"].Fill(puppiMET_pt,Event_Weight)
        h_base["h_jet_pt"].Fill(jet_pt,Event_Weight)
        h_base["h_r9_1"].Fill(phot1_r9,Event_Weight)
        h_base["h_r9_2"].Fill(phot2_r9,Event_Weight)
        h_base["h_r9_3"].Fill(phot3_r9,Event_Weight)
        h_base["h_hoe_1"].Fill(phot1_hoe,Event_Weight)
        h_base["h_hoe_2"].Fill(phot2_hoe,Event_Weight)
        h_base["h_hoe_3"].Fill(phot3_hoe,Event_Weight)

        if invmass_12 < 80 :
            h_base["h_phot2_ET_low12"].Fill(phot2_pt,Event_Weight)
            h_base["h_phot3_ET_low12"].Fill(phot3_pt,Event_Weight)

        if invmass_12 > 80 :
            h_base["h_phot2_ET_high12"].Fill(phot2_pt,Event_Weight)
            h_base["h_phot3_ET_high12"].Fill(phot3_pt,Event_Weight)

        if not isData or CRflag > 0 or (isData and (threephot_invmass < 80. or threephot_invmass > 96.)) : 
            h_base["h_threegammass"].Fill(threephot_invmass,Event_Weight)

    if select_all_but_one("h_nElectrons") : 
        h_base["h_nElectrons"].Fill(N_electrons_clean,Event_Weight)

    if select_all_but_one("h_m12") :    
        h_base["h_m12"].Fill(invmass_12,Event_Weight)
        h_base["h_eta1_invmass"].Fill(phot1_eta,Event_Weight)
        h_base["h_eta2_invmass"].Fill(phot2_eta,Event_Weight)

    if select_all_but_one("h_m13") :
        h_base["h_m13"].Fill(invmass_13,Event_Weight)

    if select_all_but_one("h_m23") :
        h_base["h_m23"].Fill(invmass_23,Event_Weight)

    if not select_all_but_one() :
        continue

    Nevts_selected += 1

    Nevts_expected += Event_Weight # Increment the number of events survived in the analyzed sample

fOut.cd()
for hist_name in list_histos:
    h_base[hist_name].Write()
fOut.Close()

print "Number of expected events for ", luminosity_norm, " in fb-1, for sample " , sample_name
print "Number of events processed = ", Nevts_per_sample
print "Number of events selected = ", Nevts_selected
print "Number of events expected = ", Nevts_expected
print "###################"
print "###################"
