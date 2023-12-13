#!/bin/bash

mH=$1
mA=$2
process=$3
direc=$4
conda activate higgs-dna
cd /vols/cms/emc21/idmStudy/MCproduction/gridpackProduction/genproductions/bin/MadGraph5_aMCatNLO/cards/iDMParameterScanUpdatedWidths_mHmA

python getWidths.py $mH $mA $process $direc 