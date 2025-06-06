
#Clean up the area
rm histos/*.root

#########
# First do the CRs 2 and 3 to get the normalization for CR1
#########

###2016 preAPV

#./histo_maker.py 0 1 0 0 finalSkim/ZThreeGamma_Signal_0.root histos/ZThreeGamma_Signal_CR1_0.root
#./histo_maker.py 0 2 0 0 finalSkim/ZThreeGamma_Signal_0.root histos/ZThreeGamma_Signal_CR2_0.root
#./histo_maker.py 0 3 0 0 finalSkim/ZThreeGamma_Signal_0.root histos/ZThreeGamma_Signal_CR3_0.root

###2016 

#./histo_maker.py 1 1 0 0 finalSkim/ZThreeGamma_Signal_1.root histos/ZThreeGamma_Signal_CR1_1.root
#./histo_maker.py 1 2 0 0 finalSkim/ZThreeGamma_Signal_1.root histos/ZThreeGamma_Signal_CR2_1.root
#./histo_maker.py 1 3 0 0 finalSkim/ZThreeGamma_Signal_1.root histos/ZThreeGamma_Signal_CR3_1.root


#data

#./histo_maker.py 0 1 0 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR1.root
#./histo_maker.py 0 2 0 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR2.root
#./histo_maker.py 0 3 0 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR3.root

#######
# Now calculate the CR correction
#######
#python calculate_CR_transfer.py 0
#python calculate_CR_transfer.py 1

######
# Now run in SR
######

#2017 preAPV simulation

./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_Signal_0.root histos/ZThreeGamma_Signal_0.root

./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_DiPhotonJets_0.root histos/ZThreeGamma_DiPhotonJets_0.root
./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_DYJetsToLL_0.root histos/ZThreeGamma_DYJetsToLL_0.root
./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_ZGToLLG_01J_0.root histos/ZThreeGamma_ZGToLLG01J_0.root
./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_GGG_0.root histos/ZThreeGamma_GGG_0.root

./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_GJets40To100_0.root histos/ZThreeGamma_GJets40To100_0.root
./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_GJets100To200_0.root histos/ZThreeGamma_GJets100To200_0.root
./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_GJets200To400_0.root histos/ZThreeGamma_GJets200To400_0.root
./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_GJets400To600_0.root histos/ZThreeGamma_GJets400To600_0.root
./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_GJets600ToInf_0.root histos/ZThreeGamma_GJets600ToInf_0.root

#2017 simulation

./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_Signal_1.root histos/ZThreeGamma_Signal_1.root

./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_DiPhotonJets_1.root histos/ZThreeGamma_DiPhotonJets_1.root
./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_DYJetsToLL_1.root histos/ZThreeGamma_DYJetsToLL_1.root
./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_ZGToLLG_01J_1.root histos/ZThreeGamma_ZGToLLG01J_1.root
./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_GGG_1.root histos/ZThreeGamma_GGG_1.root

./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_GJets40To100_1.root histos/ZThreeGamma_GJets40To100_1.root
./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_GJets100To200_1.root histos/ZThreeGamma_GJets100To200_1.root
./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_GJets200To400_1.root histos/ZThreeGamma_GJets200To400_1.root
./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_GJets400To600_1.root histos/ZThreeGamma_GJets400To600_1.root
./histo_maker.py 1 0 1 0 finalSkim/ZThreeGamma_GJets600ToInf_1.root histos/ZThreeGamma_GJets600ToInf_1.root

hadd -f histos/ZThreeGamma_GJets.root histos/ZThreeGamma_GJets*.root
rm histos/ZThreeGamma_GJets*To*.root

hadd -f histos/ZThreeGamma_Signal.root histos/ZThreeGamma_Signal_?.root
rm histos/ZThreeGamma_Signal_?.root

hadd -f histos/ZThreeGamma_DiPhotonJets.root histos/ZThreeGamma_DiPhotonJets_*.root
rm histos/ZThreeGamma_DiPhotonJets_*.root

hadd -f histos/ZThreeGamma_DYJetsToLL.root histos/ZThreeGamma_DYJetsToLL_*.root
rm histos/ZThreeGamma_DYJetsToLL_*.root

hadd -f histos/ZThreeGamma_ZGToLLG01J.root histos/ZThreeGamma_ZGToLLG01J_*.root
rm histos/ZThreeGamma_ZGToLLG01J_*.root

hadd -f histos/ZThreeGamma_GGG.root histos/ZThreeGamma_GGG_*.root
rm histos/ZThreeGamma_GGG_*.root

#2017 data
./histo_maker.py 0 0 1 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_data.root

./histo_maker.py 0 0 1 1 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_SB.root


################
#Now redo the CRs
################

# 2016 preAPV

./histo_maker.py 0 1 1 0 finalSkim/ZThreeGamma_Signal_0.root histos/ZThreeGamma_Signal_CR1_0.root
./histo_maker.py 0 2 1 0 finalSkim/ZThreeGamma_Signal_0.root histos/ZThreeGamma_Signal_CR2_0.root
./histo_maker.py 0 3 1 0 finalSkim/ZThreeGamma_Signal_0.root histos/ZThreeGamma_Signal_CR3_0.root

# 2016 preAPV

./histo_maker.py 1 1 1 0 finalSkim/ZThreeGamma_Signal_1.root histos/ZThreeGamma_Signal_CR1_1.root
./histo_maker.py 1 2 1 0 finalSkim/ZThreeGamma_Signal_1.root histos/ZThreeGamma_Signal_CR2_1.root
./histo_maker.py 1 3 1 0 finalSkim/ZThreeGamma_Signal_1.root histos/ZThreeGamma_Signal_CR3_1.root

./histo_maker.py 0 1 1 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR1.root
./histo_maker.py 0 2 1 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR2.root
./histo_maker.py 0 3 1 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR3.root


hadd -f histos/ZThreeGamma_Signal_CR1.root histos/ZThreeGamma_Signal_CR1_*.root
rm histos/ZThreeGamma_Signal_CR1_*.root

hadd -f histos/ZThreeGamma_Signal_CR2.root histos/ZThreeGamma_Signal_CR2_*.root
rm histos/ZThreeGamma_Signal_CR2_*.root

hadd -f histos/ZThreeGamma_Signal_CR3.root histos/ZThreeGamma_Signal_CR3_*.root
rm histos/ZThreeGamma_Signal_CR3_*.root
