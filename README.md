# ZThreeGamma

Instructions:

1) install a CMSSW release

cmsrel CMSSW_10_6_27
cd CMSSW_10_6_27/src
cmsenv

2) install this package

git clone git@github.com:pellicci/ZThreeGamma.git StandardModel/ZThreeGamma

3) install nanoAODTools. See https://github.com/cms-nanoAOD/nanoAOD-tools but in general:

git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools

4) compile

scram b

5) you can run the ntuple maker now

cd StandardModel/ZThreeGamma/test
python run_ntuplizer.py MC 0 /eos/user/p/pellicci/ZThreeGamma_root/2016/signal/preAPV/NANO/process.root 

to run for example on the MC for the first Run2 era (0). This will create a tree.root file

6) you can create the histos from the tree with

./histo_maker.py 0 0 0 0 tree.root histos.root

See histo_maker.py for the meaning of the bool mask
