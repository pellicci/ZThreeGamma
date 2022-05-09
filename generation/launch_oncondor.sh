#!/bin/bash

DATE=$(date +%s)

mkdir condor_subs/condor_$DATE
cp testScript_queue.sh condor_subs/condor_$DATE
cp condor.sub condor_subs/condor_$DATE

cd condor_subs/condor_$DATE
mkdir logs
mkdir outputs
condor_submit condor.sub
cd ../..

