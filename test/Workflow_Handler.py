import ROOT

ph_ID_scale_name_2016_pre  = "scale_factors/egammaEffi.txt_EGM2D_Pho_wp90_UL16.root"
pixSeed_scale_name_2016_pre  = "scale_factors/HasPix_SummaryPlot_UL16_preVFP.root"

ph_ID_scale_name_2016_post  = "scale_factors/egammaEffi.txt_EGM2D_Pho_MVA90_UL16_postVFP.root"
pixSeed_scale_name_2016_post  = "scale_factors/HasPix_SummaryPlot_UL16_postVFP.root"

ph_ID_scale_name_2017  = "scale_factors/egammaEffi.txt_EGM2D_PHO_MVA90_UL17.root"
pixSeed_scale_name_2017  = "scale_factors/HasPix_SummaryPlot_UL17.root"

ph_ID_scale_name_2018  = "scale_factors/egammaEffi.txt_EGM2D_Pho_wp90.root_UL18.root"
pixSeed_scale_name_2018  = "scale_factors/HasPix_SummaryPlot_UL18.root"


class Simplified_Workflow_Handler:

    def __init__(self,runningEra):

    	if runningEra == 0 :
    		ph_ID_scale_name = ph_ID_scale_name_2016_pre
    		pixSeed_scale_name = pixSeed_scale_name_2016_pre
    	elif runningEra == 1 :
    		ph_ID_scale_name = ph_ID_scale_name_2016_post
    		pixSeed_scale_name = pixSeed_scale_name_2016_post
    	elif runningEra == 2 :
    		ph_ID_scale_name = ph_ID_scale_name_2017
    		pixSeed_scale_name = pixSeed_scale_name_2017
    	elif runningEra == 3:
    		ph_ID_scale_name = ph_ID_scale_name_2018
    		pixSeed_scale_name = pixSeed_scale_name_2018

    	ph_ID_scale_file = ROOT.TFile(ph_ID_scale_name)
    	ph_ID_scale_TH = ROOT.TH2()
    	ph_ID_scale_TH = ph_ID_scale_file.Get("EGamma_SF2D")

    	pixseed_scale_file = ROOT.TFile(pixseed_scale_name)
    	pixseed_scale_TH = ROOT.TH2()
    	pixseed_scale_TH = pixseed_scale_file.Get("MVAID/SF_HasPix_MVAID")


    def get_photon_scale(Photon_ET,Photon_eta) :

    	ID_scale = ph_ID_scale_TH.GetBinContent(Photon_ET,Photon_eta)

    	etaBin = 1 if abs(phot1_eta) < 1.48 else 4
    	pixseed_scale = pixseed_scale_TH.GetBinContent(etaBin)

    	return ID_scale * pixseed_scale

	def get_xsec_norm(self,sample_name) :
		if runningEra == 0 :
			if "Signal" in sample_name : return float( (6225.2*0.000001/0.0337) *1000./ (199.*250.))
			if "DiPhotonJets" in sample_name : return float( 126.2 *1000./ (2359151. *(1.-2.*0.2363)))
			if "DiPhotonJets40" in sample_name : return float( 303.2 *1000./ (2499982. *(1.-2.*0.2363)))
			if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (91988603. *(1.-2.*0.1643)))
			if "ZGToLLG" in sample_name : return float( 51.1 *1000./ (27805647.*(1.-2.*0.1923)))
			if "GJets40To100" in sample_name : return float( 18540. *1000./ 8952278.)
			if "GJets100To200" in sample_name : return float( 8644. *1000./ 9332192.)
			if "GJets200To400" in sample_name : return float( 2183. *1000./ 19087322.)
			if "GJets400To600" in sample_name : return float( 260.2 *1000./ 4242991.)
			if "GJets600ToInf" in sample_name : return float( 86.58 *1000./ 4661194.)
			if "GGG" in sample_name : return float( 8.681 *1000./ (200.*500.))
		elif runningEra == 1 :
			if "Signal" in sample_name : return float( (6225.2*0.000001/0.0337) *1000./ (200.*250.))
			if "DiPhotonJets" in sample_name : return float( 126.2 *1000./ (2423396. *(1.-2.*0.2363)))
			if "DiPhotonJets40" in sample_name : return float( 303.2 *1000./ (4999973. *(1.-2.*0.2363)))
			if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (95237235.*(1.-2.*0.1643)))
			if "ZGToLLG" in sample_name : return float( 51.1 *1000./ (31606911.*(1-2.*0.1923)))
			if "GJets40To100" in sample_name : return float( 18540. *1000./ 9082742.)
			if "GJets100To200" in sample_name : return float( 8644. *1000./ 9882256.)
			if "GJets200To400" in sample_name : return float( 2183. *1000./ 19874909.)
			if "GJets400To600" in sample_name : return float( 260.2 *1000./ 4629781.)
			if "GJets600ToInf" in sample_name : return float( 86.58 *1000./ 4366096.)
			if "GGG" in sample_name : return float( 8.681 *1000./ (200.*500.))

		elif runningEra == 2 :
			if "Signal" in sample_name : return float( (6225.2*0.000001/0.0337) *1000./ (200.*500.))
			if "DiPhotonJets" in sample_name : return float( 126.2 *1000./ (4515087. *(1.-2.*0.2363)))
			if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (194627557.*(1.-2.*0.1643)))
			if "ZGToLLG" in sample_name : return float( 51.1 *1000./ (29885702.*(1-2.*0.1923)))
			if "GJets100To200" in sample_name : return float( 5034. *1000./ 10318691.)
			if "GJets200To400" in sample_name : return float( 1128. *1000./ 33668046.)
			if "GJets400To600" in sample_name : return float( 124.8 *1000./ 9870485.)
			if "GJets600ToInf" in sample_name : return float( 40.72 *1000./ 8330226.)
			if "GGG" in sample_name : return float( 8.681 *1000./ (200.*500.))

		elif runningEra == 3 :
			if "Signal" in sample_name : return float( (6225.2*0.000001/0.0337) *1000./ (199.*500.))

		return 1.
