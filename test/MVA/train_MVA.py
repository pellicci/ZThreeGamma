import ROOT

ROOT.gROOT.SetBatch(True)

fIn_bkg  = ROOT.TFile("../histos/ZThreeGamma_SB.root")
tree_bkg = fIn_bkg.Get("minitree")
 
fIn_sig  = ROOT.TFile("../histos/ZThreeGamma_Signal.root")
tree_sig = fIn_sig.Get("minitree")

fOut = ROOT.TFile("trained/Nominal_training.root","RECREATE")

ROOT.TMVA.Tools.Instance()

factory = ROOT.TMVA.Factory("TMVAClassification", fOut,":".join(["!V","Transformations=G,D","AnalysisType=Classification"]))

dataloader = ROOT.TMVA.DataLoader()
#dataloader.AddVariable("Phot1_ET/M_ggg","F") # Both Float and Double variable types must be indicated as F
#dataloader.AddVariable("Phot2_ET/M_ggg","F")
#dataloader.AddVariable("Phot3_ET/M_ggg","F")
dataloader.AddVariable("Phot1_hoe","F")
dataloader.AddVariable("Phot2_hoe","F")
dataloader.AddVariable("Phot3_hoe","F")
dataloader.AddVariable("Phot1_r9","F")
dataloader.AddVariable("Phot2_r9","F")
dataloader.AddVariable("Phot3_r9","F")
dataloader.AddVariable("Phot1_iso","F")
dataloader.AddVariable("Phot2_iso","F")
dataloader.AddVariable("Phot3_iso","F")
dataloader.AddVariable("MET_pT","F")
dataloader.AddVariable("Z_pT","F")
dataloader.AddVariable("Sum_gam_id","F")

sig_weight = 1.
bkg_weight = 1.

dataloader.AddSignalTree(tree_sig, sig_weight)
dataloader.AddBackgroundTree(tree_bkg, bkg_weight)

dataloader.SetWeightExpression("Event_Weight")

mycutSig = ROOT.TCut("")
mycutBkg = ROOT.TCut("")

#method_btd  = factory.BookMethod(dataloader, ROOT.TMVA.Types.kKNN, "kNN", ":".join(["H","!V","VarTransform=U,G,D","nkNN=3000"]))
method_btd  = factory.BookMethod(dataloader, ROOT.TMVA.Types.kBDT, "BDT", ":".join(["H","!V","VarTransform=U,G,D","NTrees=800","MinNodeSize=2.5%","AdaBoostBeta=0.2","MaxDepth=3","BoostType=AdaBoost","NegWeightTreatment=IgnoreNegWeightsInTraining"]))

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

fOut.Close()

