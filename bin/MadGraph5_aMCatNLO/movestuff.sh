#!/bin/bash

for i in {1..20}; 
do 
    mv h2h2lPlM_lem_BP$i /eos/user/e/ecurtis/idmStudy/myFiles/gridpacks/h2h2lPlM_lem/h2h2lPlM_lem_BP$i/
done

for i in {1..20}; 
do 
    mv h2h2lPlM_lem_BP$i.log /eos/user/e/ecurtis/idmStudy/myFiles/gridpacks/h2h2lPlM_lem/h2h2lPlM_lem_BP$i/
done

for i in {1..20}; 
do 
    mv h2h2lPlM_lem_BP${i}_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz /eos/user/e/ecurtis/idmStudy/myFiles/gridpacks/h2h2lPlM_lem/h2h2lPlM_lem_BP$i/
done