#!/bin/bash

mH=$1
mA=$2
mHch=$3
process=$4
direc=$5
conda activate higgs-dna
cd /vols/cms/emc21/idmStudy/MCproduction/gridpackProduction/genproductions/bin/MadGraph5_aMCatNLO/cards/iDMParameterScanUpdatedWidths

python getWidths.py $mH $mA $mHch $process $direc 