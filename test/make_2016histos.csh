
#Clean up the area
rm histos/*.root

#########
# First do the CRs 2 and 3 to get the normalization for CR1
#########
./histo_maker.py 0 1 0 finalSkim/ZThreeGamma_Signal.root histos/ZThreeGamma_Signal_CR1.root
./histo_maker.py 0 1 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR1.root

./histo_maker.py 0 2 0 finalSkim/ZThreeGamma_Signal.root histos/ZThreeGamma_Signal_CR2.root
./histo_maker.py 0 2 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR2.root

./histo_maker.py 0 3 0 finalSkim/ZThreeGamma_Signal.root histos/ZThreeGamma_Signal_CR3.root
./histo_maker.py 0 3 0 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR3.root

#######
# Now calculate the CR correction
#######
python calculate_CR_transfer.py


######
# Now run in SR
######

#2016 simulation

./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_Signal.root histos/ZThreeGamma_Signal.root
./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_DiPhotonJets.root histos/ZThreeGamma_DiPhotonJets.root
./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_DYJetsToLL.root histos/ZThreeGamma_DYJetsToLL.root
./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_ZGToLLG_01J.root histos/ZThreeGamma_ZGToLLG01J.root

./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_GJets40To100.root histos/ZThreeGamma_GJets40To100.root
./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_GJets100To200.root histos/ZThreeGamma_GJets100To200.root
./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_GJets200To400.root histos/ZThreeGamma_GJets200To400.root
./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_GJets400To600.root histos/ZThreeGamma_GJets400To600.root
./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_GJets600ToInf.root histos/ZThreeGamma_GJets600ToInf.root

hadd -f histos/ZThreeGamma_GJets.root histos/ZThreeGamma_GJets*.root
rm histos/ZThreeGamma_GJets*To*.root

#2016 data and merge

./histo_maker.py 0 0 1 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_data.root

################
#Now redo the CRs
################

./histo_maker.py 0 1 1 finalSkim/ZThreeGamma_Signal.root histos/ZThreeGamma_Signal_CR1.root
./histo_maker.py 0 1 1 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR1.root

./histo_maker.py 0 3 1 finalSkim/ZThreeGamma_Signal.root histos/ZThreeGamma_Signal_CR3.root
./histo_maker.py 0 3 1 finalSkim/ZThreeGamma_DoubleEG.root histos/ZThreeGamma_CR3.root
