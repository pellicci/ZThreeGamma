#!/bin/sh

echo "Job submitted on host `hostname` on `date`"
echo ">>> arguments: $@"

#this is necessary only if EOS access is required
export X509_USER_PROXY=/afs/cern.ch/user/p/pellicci/voms_proxy/x509up_u28550

### Required parameters #####
COUNT=$1
YEAR=$2
SUFFIX=$4
OUTDIR=$5
ANALYZER=$6

if [[ "$3" == "True" ]]
then
    ISDATA="data"
else
    ISDATA="MC"
fi

### Transfer files, prepare directory ###
TOPDIR=$PWD

export SCRAM_ARCH=slc7_amd64_gcc10
export CMSSW_VERSION=CMSSW_12_6_0_patch1
source /cvmfs/cms.cern.ch/cmsset_default.sh

# temporary fix
tar -xzf source.tar.gz
mv $CMSSW_VERSION tmp_source
scram project CMSSW $CMSSW_VERSION
cp -r tmp_source/src/* $CMSSW_VERSION/src
cd $CMSSW_VERSION/src
eval `scram runtime -sh`

cmsenv
scramv1 b -j8
INPUT_TXT_FILENAME=input_${SUFFIX}_${COUNT}.txt
cp $TOPDIR/${INPUT_TXT_FILENAME} ${INPUT_TXT_FILENAME}

echo "Inputs: "
echo $ANALYZER $SUFFIX $ISDATA $COUNT
echo "PATH: "
echo $PATH
echo "Starting working dir: "
pwd
cd StandardModel/ZThreeGamma
cp test/keep_and_drop.txt .
echo "Working dir: "
pwd
mv ../../input_${SUFFIX}_${COUNT}.txt ./
echo "Input file list: "
cat $INPUT_TXT_FILENAME

[ ! -d outDir ] && mkdir outDir

### Run the analyzer

COUNTER=0
while IFS= read NANOAOD
do
    # xrdcp to local src folder first
    # analyzer is upto 100x-200x faster than xrd streaming. Ziheng
    echo "Copying ${NANOAOD} locally"
    xrdcp ${NANOAOD} ./temp.root
    XRDEXIT=$?
    if [[ $XRDEXIT -ne 0 ]]; then
        rm *.root
        echo "exit code $XRDEXIT, failure in xrdcp"
        exit $XRDEXIT
    fi

    python test/${ANALYZER} ${ISDATA} runningEra=${YEAR} temp.root
    mv tree.root outDir/tree_${COUNTER}.root
    rm *.root
    COUNTER=$((COUNTER+1))

done <$INPUT_TXT_FILENAME

ls
ls outDir/

### Copy output and cleanup ###
FILE=output_${SUFFIX}_${COUNT}.root
scripts/haddnano.py ${FILE} outDir/*root

xrdcp -f ${FILE} ${OUTDIR}/${FILE} 2>&1
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
  rm *.root
  echo "exit code $XRDEXIT, failure in xrdcp"
  exit $XRDEXIT
fi
rm ${FILE}
rm -rf outDir
