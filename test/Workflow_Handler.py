import ROOT
import math

ph_ID_scale_name_2016_pre  = "scale_factors/egammaEffi.txt_EGM2D_Pho_wp90_UL16.root"
pixSeed_scale_name_2016_pre  = "scale_factors/HasPix_SummaryPlot_UL16_preVFP.root"

ph_ID_scale_name_2016_post  = "scale_factors/egammaEffi.txt_EGM2D_Pho_MVA90_UL16_postVFP.root"
pixSeed_scale_name_2016_post  = "scale_factors/HasPix_SummaryPlot_UL16_postVFP.root"

ph_ID_scale_name_2017  = "scale_factors/egammaEffi.txt_EGM2D_PHO_MVA90_UL17.root"
pixSeed_scale_name_2017  = "scale_factors/HasPix_SummaryPlot_UL17.root"

ph_ID_scale_name_2018  = "scale_factors/egammaEffi.txt_EGM2D_Pho_wp90.root_UL18.root"
pixSeed_scale_name_2018  = "scale_factors/HasPix_SummaryPlot_UL18.root"

pt_binning = dict()
pt_binning["lead2016"]  = [32.,33.,35.,40.,45.,50.,60.,70.,90.]
pt_binning["trail2016"] = [20.,32.,34.,36.,38.,40.,45.,50.,55.]
pt_binning["lead2017"]  = [32.,33.,35.,37.,40.,45.,50.,60.,70.]
pt_binning["trail2017"] = [20.,25.,28.,31.,40.,70.]
pt_binning["lead2018"]  = [32.,35.,37.,40.,45.,50.,60.,70.,90.]
pt_binning["trail2018"]  = [20.,25.,28.,31.,35.,40.,45.,50.,60.]


trigscale = dict()
trigscale["leadingEB2016"]    = [ [0.480261, 0.911612] , [0.544853,0.964408], [0.564528,0.973082] , [0.584602,0.978494], [0.610664,0.981905] , [0.638541,0.982553] , [0.679178,0.986766] , [0.719895,0.986766] ]
trigscale["leadingEB2016err"] = [ [0.005, 0.0005] , [0.006,0.0004], [0.003,0.0002] , [0.002,0.0001], [0.002,0.0001] , [0.003,0.0002] , [0.006,0.0003] , [0.008,0.0004] ]

trigscale["leadingEE2016"]    = [ [0.595211,0.853852] , [0.702697,0.950491], [0.734526,0.965209] , [0.760539,0.970964], [0.778439,0.973743] , [0.791388,0.977689] , [0.81457,0.981832] , [0.837738,0.989488] ]
trigscale["leadingEE2016err"] = [ [0.006,0.001] , [0.007,0.001], [0.003,0.0006] , [0.002,0.0004], [0.003,0.0005] , [0.004,0.0006] , [0.007,0.001] , [0.009,0.001] ]

trigscale["leadingEB2016OR"]    = [ [0.917161,0.917161] , [0.969697,0.969697], [0.977014,0.977014] , [0.980632,0.980632], [0.983649,0.983649] , [0.984346,0.984346] , [0.98573,0.98573] , [0.98907,0.98907] ]
trigscale["leadingEB2016ORerr"] = [ [0.0004,0.0004] , [0.0003,0.0003], [0.0001,0.0001] , [0.0001,0.0001], [0.0001,0.0001] , [0.0001,0.0001] , [0.0002,0.0002] , [0.0003,0.0003] ]

trigscale["trailEB2016"]    = [ [0.520538,0.957582], [0.544783,0.96933] , [0.552613,0.971038], [0.569686,0.973016] , [0.57511,0.975327] , [0.586177,0.977557] , [0.612741,0.978469], [0.635098,0.979083] ]
trigscale["trailEB2016err"] = [ [0.004,0.004], [0.006,0.004] , [0.006,0.004], [0.005,0.004] , [0.005,0.004] , [0.003,0.004] , [0.003,0.004] , [0.005,0.004] ]

trigscale["trailEE2016"]    = [ [0.685109,0.952053], [0.697586,0.960736] , [0.708077,0.963011], [0.71455,0.962529] , [0.728204,0.965013] , [0.7459,0.965534] , [0.761913,0.966361] , [0.769585,0.965761] ]
trigscale["trailEE2016err"] = [ [0.01,0.02], [0.01,0.02] , [0.01,0.02], [0.01,0.02] , [0.01,0.02] , [0.01,0.02] , [0.01,0.02], [0.02,0.02] ]

trigscale["trailEB2016OR"]    = [ [0.973687,0.973687], [0.978161,0.978161] , [0.979632,0.979632], [0.980581,0.980581] , [0.981697,0.981697] , [0.982505,0.982505] , [0.983331,0.983331], [0.984008,0.984008] ]
trigscale["trailEB2016ORerr"] = [ [0.005,0.005], [0.005,0.005] , [0.005,0.005], [0.005,0.005] , [0.005,0.005] , [0.005,0.005] , [0.005,0.005] , [0.005,0.005] ]

trigscale["leadingEB2017"]    = [ [0.697427,0.764902] , [0.882715,0.930524], [0.894138,0.938207] , [0.902827,0.943564], [0.912114,0.947708] , [0.915718,0.949471] , [0.920406,0.949001] , [0.924396,0.95082] ]
trigscale["leadingEB2017err"] = [ [0.001, 0.001] , [0.001,0.001], [0.001,0.001] , [0.001,0.001], [0.001,0.001] , [0.001,0.001] , [0.001,0.001] , [0.001,0.001] ]

trigscale["leadingEE2017"]    = [ [0.533179,0.587245] , [0.78167,0.860594], [0.853343,0.904747] , [0.882869,0.926744], [0.901054,0.942814] , [0.914075,0.951324] , [0.921084,0.953806] , [0.933343,0.958042] ]
trigscale["leadingEE2017err"] = [ [0.002,0.001] , [0.001,0.001], [0.001,0.001] , [0.001,0.001], [0.001,0.001] , [0.001,0.001] , [0.001,0.001] , [0.002,0.001] ]

trigscale["trailEB2017"]    = [ [0.931975,0.931975], [0.959115,0.959115] , [0.96881,0.96881], [0.975143,0.975143] , [0.970157,0.970157] ]
trigscale["trailEB2017err"] = [ [0.01,0.01], [0.02,0.02] , [0.01,0.01], [0.01,0.01] , [0.01,0.01] ]

trigscale["trailEE2017"]    = [ [0.842708,0.842708], [0.945462,0.945462] , [0.962701,0.962701], [0.965889,0.965889] , [0.969626,0.969626] ]
trigscale["trailEE2017err"] = [ [0.02,0.02], [0.02,0.02] , [0.02,0.02], [0.01,0.01] , [0.01,0.01] ]

trigscale["leadingEB2018"]    = [ [0.8612698995,0.8612698995] , [0.9591566003,0.9591566003], [0.9661504394,0.9661504394] , [0.9713429409,0.9713429409], [0.9766069398,0.9766069398] , [0.9785793731,0.9785793731] , [0.9784872329,0.9784872329] , [0.9807043393,0.9807043393] ]
trigscale["leadingEB2018err"] = [ [0.003, 0.003] , [0.001,0.001], [0.001,0.001] , [0.001,0.001], [0.001,0.001] , [0.002,0.002] , [0.003,0.003] , [0.001,0.001] ]

trigscale["leadingEE2018"]    = [ [0.8336632168,0.8453711721] , [0.9593305114,0.9712187003], [0.9639324466,0.9768360010] , [0.9673347931,0.9803619699], [0.9730845967,0.9838732468] , [0.9700713622,0.9849675199] , [0.9753541182,0.9905641943] , [0.9778381112,0.9891408232] ]
trigscale["leadingEE2018err"] = [ [0.006,0.002] , [0.001,0.001], [0.001,0.001] , [0.001,0.001], [0.001,0.004] , [0.001,0.01] , [0.003,0.003] , [0.003,0.003] ]

trigscale["trailEB2018"]    = [ [0.9672297042,0.9672297042], [0.9805682395,0.9805682395] , [0.9857864878,0.9857864878], [0.9899655333,0.9899655333] , [0.9926847217,0.9926847217] , [0.9936363464,0.9936363464] , [0.9938550364,0.9938550364], [0.9942535185,0.9942535185] ]
trigscale["trailEB2018err"] = [ [0.001,0.001], [0.003,0.003] , [0.003,0.003], [0.001,0.001] , [0.001,0.001] , [0.001,0.001] , [0.002,0.002] , [0.001,0.001] ]

trigscale["trailEE2018"]    = [ [0.9121171624,0.9433319000], [0.9543055879,0.9836486488] , [0.9584879018,0.9849810016], [0.9665292836,0.9898516787] , [0.9724877347,0.9925685115] , [0.9756256530,0.9934337616] , [0.9794385124,0.9932323204] , [0.9785902688,0.9933956724] ]
trigscale["trailEE2018err"] = [ [0.004,0.004], [0.001,0.002] , [0.001,0.004], [0.001,0.001] , [0.001,0.001] , [0.001,0.001] , [0.001,0.001] , [0.001,0.001] ]

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

		ID_scale     = self.ph_ID_scale_TH.GetBinContent( self.ph_ID_scale_TH.GetXaxis().FindBin(Photon_eta) , self.ph_ID_scale_TH.GetYaxis().FindBin(Photon_ET) )
		ID_scale_err = self.ph_ID_scale_TH.GetBinError( self.ph_ID_scale_TH.GetXaxis().FindBin(Photon_eta) , self.ph_ID_scale_TH.GetYaxis().FindBin(Photon_ET) )

		etaBin = 1 if abs(Photon_eta) < 1.48 else 4
		pixseed_scale = self.pixseed_scale_TH.GetBinContent(etaBin)

		return ID_scale * pixseed_scale , ID_scale_err

	def get_ET_bin_fortrig(self,Photon_ET,isLeading) :

		lookup_word = ""
		if isLeading :
			lookup_word = "lead"
		else :
			lookup_word = "trail"

		if self.runningEra < 2 :
			lookup_word = lookup_word + "2016"
		elif self.runningEra == 2:
			lookup_word = lookup_word + "2017"
		elif self.runningEra == 3:
			lookup_word = lookup_word + "2018"

		ptbin = [i for i in range(len(pt_binning[lookup_word])) if pt_binning[lookup_word][i] < Photon_ET][-1]
		if ptbin > (len(pt_binning[lookup_word]) - 2) :
			return ptbin - 1
		return ptbin

	def get_R9_bin_fortrig(self,Photon_r9,Photon_eta) :

		if Photon_r9 < 0.88 and abs(Photon_eta) < 1.5 :
			return 0
		if Photon_r9 < 0.93 and abs(Photon_eta) >= 1.5 :
			return 0
		else :
			return 1

	def get_trig_scale(self,Photon_ET,Photon_eta,Photon_r9,isLeading,isBB) :

		ET_bin = self.get_ET_bin_fortrig(Photon_ET,isLeading)
		R9_bin = self.get_R9_bin_fortrig(Photon_r9,Photon_eta)

		trigweight = 1.
		trigweight_err = 0.

		lookup_word = ""
		if isLeading :
			lookup_word = "leading"
		else :
			lookup_word = "trail"
		if Photon_eta < 1.5 :
			lookup_word = lookup_word + "EB"
		else :
			lookup_word = lookup_word + "EE"

		if self.runningEra < 2 :
			if isBB :
				lookup_word = lookup_word + "2016OR"
			else :
				lookup_word = lookup_word + "2016"
		elif self.runningEra == 2 :
			lookup_word = lookup_word + "2017"			
		elif self.runningEra == 3 :
			lookup_word = lookup_word + "2018"			
		
		trigweight     = trigscale[lookup_word][ET_bin][R9_bin]
		trigweight_err = trigscale[lookup_word+"err"][ET_bin][R9_bin]

		return trigweight , trigweight_err

	def get_xsec_norm(self, sample_name) :

		if self.runningEra == 0 :
			if "Signal" in sample_name : return float( (1981.0*0.0000001/0.033658) *1000./ (248.*400.))
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
			if "Signal" in sample_name : return float( (1981.0*0.0000001/0.033658) *1000./ (247.*400.))
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
			if "Signal" in sample_name : return float( (1981.0*0.0000001/0.033658) *1000./ (250.*400.))
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
			if "Signal" in sample_name : return float( (1981.0*0.0000001/0.033658) *1000./ (250.*400.))
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
