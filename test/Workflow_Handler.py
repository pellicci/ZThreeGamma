import ROOT

ph_ID_scale_name_2016_pre  = "scale_factors/egammaEffi.txt_EGM2D_Pho_wp90_UL16.root"
pixSeed_scale_name_2016_pre  = "scale_factors/HasPix_SummaryPlot_UL16_preVFP.root"

ph_ID_scale_name_2016_post  = "scale_factors/egammaEffi.txt_EGM2D_Pho_MVA90_UL16_postVFP.root"
pixSeed_scale_name_2016_post  = "scale_factors/HasPix_SummaryPlot_UL16_postVFP.root"

ph_ID_scale_name_2017  = "scale_factors/egammaEffi.txt_EGM2D_PHO_MVA90_UL17.root"
pixSeed_scale_name_2017  = "scale_factors/HasPix_SummaryPlot_UL17.root"

ph_ID_scale_name_2018  = "scale_factors/egammaEffi.txt_EGM2D_Pho_wp90.root_UL18.root"
pixSeed_scale_name_2018  = "scale_factors/HasPix_SummaryPlot_UL18.root"

class Workflow_Handler:

	def __init__(self,myrunningEra):

		self.runningEra = myrunningEra

		if self.runningEra == 0 :
			ph_ID_scale_name = ph_ID_scale_name_2016_pre
			pixSeed_scale_name = pixSeed_scale_name_2016_pre
			self.lumi_norm = 19.52
		elif self.runningEra == 1 :
			ph_ID_scale_name = ph_ID_scale_name_2016_post
			pixSeed_scale_name = pixSeed_scale_name_2016_post
			self.lumi_norm = 16.81
		elif self.runningEra == 2 :
			ph_ID_scale_name = ph_ID_scale_name_2017
			pixSeed_scale_name = pixSeed_scale_name_2017
			self.lumi_norm = 41.48
		elif self.runningEra == 3:
			ph_ID_scale_name = ph_ID_scale_name_2018
			pixSeed_scale_name = pixSeed_scale_name_2018
			self.lumi_norm = 59.83

		self.ph_ID_scale_file = ROOT.TFile(ph_ID_scale_name)
		self.ph_ID_scale_TH = self.ph_ID_scale_file.Get("EGamma_SF2D")

		self.pixseed_scale_file = ROOT.TFile(pixSeed_scale_name)
		self.pixseed_scale_TH = self.pixseed_scale_file.Get("MVAID/SF_HasPix_MVAID")

	def get_lumi_norm(self) :
		return self.lumi_norm

	def get_photon_scale(self,Photon_ET,Photon_eta) :

		if Photon_ET < 20. :
			Photon_ET = 20.5

		ID_scale = self.ph_ID_scale_TH.GetBinContent( self.ph_ID_scale_TH.GetXaxis().FindBin(Photon_eta) , self.ph_ID_scale_TH.GetYaxis().FindBin(Photon_ET) )

		etaBin = 1 if abs(Photon_eta) < 1.48 else 4
		pixseed_scale = self.pixseed_scale_TH.GetBinContent(etaBin)

		return ID_scale * pixseed_scale

	def get_xsec_norm(self, sample_name) :

		if self.runningEra == 0 :
			if "Signal" in sample_name : return float( (6404.0*0.000001/0.0337) *1000./ (248.*400.))
			if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (90947213. *(1.-2.*0.1643)))
			if "ZGToLLG" in sample_name : return float( 55.48 *1000./ (23275543.*(1.-2.*0.1847)))
			if "DiPhotonJets" in sample_name : return float( 126.2 *1000./ (2365165. *(1.-2.*0.2363)))
			if "DiPhotonJets40" in sample_name : return float( 303.2 *1000./ (2499982.))
			if "GJets40To100" in sample_name : return float( 18540. *1000./ 8246771.)
			if "GJets100To200" in sample_name : return float( 8644. *1000./ 8461618.)
			if "GJets200To400" in sample_name : return float( 2183. *1000./ 19037560.)
			if "GJets400To600" in sample_name : return float( 260.2 *1000./ 4338294.)
			if "GJets600ToInf" in sample_name : return float( 86.58 *1000./ 4624766.)
			if "GGG" in sample_name : return float( 8.681 *1000./ (200.*500.))
		elif self.runningEra == 1 :
			if "Signal" in sample_name : return float( (6404.0*0.000001/0.0337) *1000./ (247.*400.))
			if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (71839442.*(1.-2.*0.1643)))
			if "ZGToLLG" in sample_name : return float( 55.48 *1000./ (31562465.*(1-2.*0.1847)))
			if "DiPhotonJets" in sample_name : return float( 126.2 *1000./ (2420370. *(1.-2.*0.2363)))
			if "DiPhotonJets40" in sample_name : return float( 303.2 *1000./ (2330985.))
			if "GJets40To100" in sample_name : return float( 18540. *1000./ 8910882.)
			if "GJets100To200" in sample_name : return float( 8644. *1000./ 9624073.)
			if "GJets200To400" in sample_name : return float( 2183. *1000./ 18315845.)
			if "GJets400To600" in sample_name : return float( 260.2 *1000./ 4475962.)
			if "GJets600ToInf" in sample_name : return float( 86.58 *1000./ 4366096.)
			if "GGG" in sample_name : return float( 8.681 *1000./ (200.*500.))
		elif self.runningEra == 2 :
			if "Signal" in sample_name : return float( (6404.0*0.000001/0.0337) *1000./ (250.*400.))
			if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (195529774.*(1.-2.*0.1643)))
			if "ZGToLLG" in sample_name : return float( 51.1 *1000./ (29890946.*(1-2.*0.1923)))
			if "DiPhotonJets" in sample_name : return float( 82.51 *1000./ (29676800.))
			if "DiPhotonJets40" in sample_name : return float( 303.2 *1000./ (3432778.))
			if "GJets100To200" in sample_name : return float( 5034. *1000./ 10034997.)
			if "GJets200To400" in sample_name : return float( 1128. *1000./ 33884844.)
			if "GJets400To600" in sample_name : return float( 126.2 *1000./ 9022800.)
			if "GJets600ToInf" in sample_name : return float( 41.31 *1000./ 8330226.)
			if "GGG" in sample_name : return float( 8.681 *1000./ (200.*500.))
		elif self.runningEra == 3 :
			if "Signal" in sample_name : return float( (6404.0*0.000001/0.0337) *1000./ (250.*400.))
			if "DYJetsToLL" in sample_name : return float( 6404.0 *1000./ (195510810.*(1.-2.*0.1643)))
			if "ZGToLLG" in sample_name : return float( 51.1 *1000./ (29919798.*(1-2.*0.1923)))
			if "DiPhotonJets" in sample_name : return float( 82.51 *1000./ (29948772.))
			if "DiPhotonJets40" in sample_name : return float( 303.2 *1000./ (4995967.))
			if "GJets100To200" in sample_name : return float( 5034. *1000./ 14278296.)
			if "GJets200To400" in sample_name : return float( 1128. *1000./ 44247215.)
			if "GJets400To600" in sample_name : return float( 126.2 *1000./ 13373955.)
			if "GJets600ToInf" in sample_name : return float( 41.31 *1000./ 11584420.)
			if "GGG" in sample_name : return float( 8.681 *1000./ (200.*500.))

		return 1.
