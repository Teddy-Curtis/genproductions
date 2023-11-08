import os
import numpy as np
import sys

# Here I need to read in *_run_card, *_customizecards, *_extramodels
# then create a new proc_card.

# These are the custom parameters for the run
mH = 80
base_dir = f"mH{mH}"
run_prefix = 'h2h2lPlMnunu'
# put a \n in between each line
defines = 'define l+ = e+ mu+ \ndefine l- = e- mu- \ndefine vl = ve vm vt \ndefine vl~ = ve~ vm~ vt~'
process = 'generate p p > h2 h2 l+ l- vl vl~'


other_run_prefix = "h2h2lPlM"


mAs = np.arange(mH, mH + 120, 10)
mHchs = np.arange(mH, mH + 120, 10)


os.makedirs(f"{base_dir}/{run_prefix}", exist_ok = True)

files_to_copy = ['_run_card.dat', '_customizecards.dat', '_extramodels.dat']

def replaceInFile(file, defines, process, run_name, mH, mA, mHch):
    file = file.replace("<DEFINE>", defines)
    file = file.replace("<PROCESS>", process)
    file = file.replace("<RUN_NAME>", run_name)
    file = file.replace("<MH2>", str(mH))
    file = file.replace("<MH3>", str(mA))
    file = file.replace("<MHPM>", str(mHch))
    file = file.replace("<LAM2>", str(0.0))
    file = file.replace("<LAML>", str(0.0000000000001))
    return file

def readFile(filename):
    with open(filename, 'r') as f:
        file = f.read()
    return file

def saveFile(file, filename):
    with open(filename, 'w') as f:
        f.write(file)

# First I will just copy the required files over

for i, mA in enumerate(mAs):
    for j, mHch in enumerate(mHchs):
        if not ((mH < mA) & (mA < mHch)):
            continue
        if mA - mH > 80:
            continue
        
        print(f"{mH}, {mA}, {mHch}")
        run_name = f'{run_prefix}_mH{mH}_mA{mA}_mHch{mHch}'
        run_directory = f"{base_dir}/{run_prefix}/{run_name}"
        try:
            os.mkdir(run_directory)
        except:
            pass

        other_run_name = f'{other_run_prefix}_mH{mH}_mA{mA}_mHch{mHch}'
        other_proc_dir = f"{base_dir}/{other_run_prefix}/{other_run_name}"


        for file_suffix in files_to_copy:
            file_to_copy = f"{other_proc_dir}/{other_run_name}{file_suffix}"
            file = readFile(file_to_copy)
            # Now save it in the new place
            filename = f'{run_directory}/{run_name}{file_suffix}'
            print(file_to_copy)
            print(filename)
            saveFile(file, filename)
        
        # Now I need to make the _proc_card.dat file for each point
        file_suffix = "_proc_card.dat"
        file = readFile(file_suffix)
        file = replaceInFile(file, defines, process, run_name, mH, mA, mHch)
        filename = f'{run_name}{file_suffix}'
        file_dir = f'{run_directory}/{filename}'
        saveFile(file, file_dir)