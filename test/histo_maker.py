#!/usr/bin/env python

import ROOT
import argparse
import math

def get_xsec_norm(runningEra, sample_name) :
	if runningEra == 0 :
		if "Signal" in sample_name : return float( (6225.2*0.000001/0.0337) *1000./ (199.*250.))
        if "DiPhotonJets" in sample_name : return float( 126.2 *1000./ (2359151. *(1-2*0.2363)))
        if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (91988603. *(1-2*0.1643)))
        if "ZGToLLG" in sample_name : return float( 51.1 *1000./ (27805647. *(1-2*0.1923)))

	return 1.

p = argparse.ArgumentParser(description='Select whether to fill the histograms after pre-selection or selection')
p.add_argument('runningEra_option', help='Type <<0>> for 2016, <<1>> for 2017, <<2>> for 2018, <<3>> for combination of years')
p.add_argument('inputfile_option', help='Provide input file name')
p.add_argument('outputfile_option', help='Provide output file name')
args = p.parse_args()

runningEra = int(args.runningEra_option)
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
if "SingleMu" in sample_name or "SingleEle" in sample_name :
    isData = True
    print "Analyzing a data sample..."
else :
	print "Analyzing a MC sample..."

#get the MC normalization
Norm_xsec = get_xsec_norm(runningEra, sample_name)

#prepare the histos
h_base = dict()

list_histos = ["h_threegammass","h_phot1_ET","h_phot2_ET","h_phot3_ET","h_nElectrons","h_deltaR_Zgam","h_twogammass"]

h_base[list_histos[0]] = ROOT.TH1F(list_histos[0], "M_{#gamma#gamma#gamma}", 60, 60., 120.)
h_base[list_histos[1]] = ROOT.TH1F(list_histos[1], "E_{T,#gamma_{1}}", 60, 0., 120.)
h_base[list_histos[2]] = ROOT.TH1F(list_histos[2], "E_{T,#gamma_{2}}", 60, 0., 120.)
h_base[list_histos[3]] = ROOT.TH1F(list_histos[3], "E_{T,#gamma_{3}}", 60, 0., 120.)
h_base[list_histos[4]] = ROOT.TH1F(list_histos[4], "N_{ele}", 10, -0.5, 9.5)
h_base[list_histos[5]] = ROOT.TH1F(list_histos[5], "#Delta R 1,2-3", 15, -1., 10.)
h_base[list_histos[6]] = ROOT.TH1F(list_histos[6], "M_{#gamma#gamma}", 60, 40., 120.)

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

    phot1_pt = mytree.Photon_pt[0]
    phot1_eta = mytree.Photon_eta[0]
    phot1_phi = mytree.Photon_phi[0]

    phot2_pt = mytree.Photon_pt[1]
    phot2_eta = mytree.Photon_eta[1]
    phot2_phi = mytree.Photon_phi[1]

    phot3_pt = mytree.Photon_pt[2]
    phot3_eta = mytree.Photon_eta[2]
    phot3_phi = mytree.Photon_phi[2]

    phot1_FourMom.SetPtEtaPhiM(phot1_pt,phot1_eta,phot1_phi,0.)
    phot2_FourMom.SetPtEtaPhiM(phot2_pt,phot2_eta,phot2_phi,0.)
    phot3_FourMom.SetPtEtaPhiM(phot3_pt,phot3_eta,phot3_phi,0.)

    twophot_FourMom = phot1_FourMom + phot2_FourMom
    deltaR_Zgam = twophot_FourMom.DeltaR(phot3_FourMom)
    threephot_FourMom = phot1_FourMom + phot2_FourMom + phot3_FourMom

    twophot_invmass = twophot_FourMom.M()
    threephot_invmass = threephot_FourMom.M()

    #Determine the event weights
    if not isData :
    	MC_Weight = mytree.genWeight
        PU_Weight = mytree.puWeight # Add Pile Up weight

        Event_Weight = norm_factor*MC_Weight*PU_Weight/math.fabs(MC_Weight) # Just take the sign of the gen weight
    else :
    	Event_Weight = 1.

    N_electrons_clean = 0.
    for elecount in xrange(mytree.nElectron) :
        if mytree.Electron_mvaFall17V1Iso_WP90[elecount] and mytree.Electron_pt[elecount] > 5. :
    		N_electrons_clean += 1.
    h_base["h_nElectrons"].Fill(N_electrons_clean,Event_Weight)

    if N_electrons_clean > 0. :
    	continue

    if not mytree.Photon_mvaID_WP80[2] :
        continue

    h_base["h_threegammass"].Fill(threephot_invmass,Event_Weight)
    h_base["h_phot1_ET"].Fill(phot1_pt,Event_Weight)
    h_base["h_phot2_ET"].Fill(phot2_pt,Event_Weight)
    h_base["h_phot3_ET"].Fill(phot3_pt,Event_Weight)
    h_base["h_deltaR_Zgam"].Fill(deltaR_Zgam,Event_Weight)
    h_base["h_twogammass"].Fill(twophot_invmass,Event_Weight)

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
