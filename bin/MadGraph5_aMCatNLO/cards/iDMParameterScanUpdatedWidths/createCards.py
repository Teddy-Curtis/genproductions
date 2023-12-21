import os
import numpy as np
import sys

# These are the custom parameters for the run
mH = 70
base_dir = f"mH{mH}"
run_prefix = 'h2h2lPlM'
# put a \n in between each line
defines = 'define l+ = e+ mu+ \ndefine l- = e- mu- \ndefine vl = ve vm vt \ndefine vl~ = ve~ vm~ vt~'
process = 'generate p p > h2 h2 l+ l-'


mAs = np.arange(mH, mH + 120, 10)
mHchs = np.arange(mH, mH + 120, 10)


# Check if directory already exists as we don't want to overwrite them 
# if the decays have already been found! 
if os.path.exists(f"{base_dir}/{run_prefix}"):
    print(f"Directory already exists, exiting so that it doesn't overwrite the decays that have been found!")
    sys.exit(0)

os.makedirs(f"{base_dir}/{run_prefix}", exist_ok = True)



files = ['_proc_card.dat', '_run_card.dat', '_customizecards.dat', '_extramodels.dat']

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




for i, mA in enumerate(mAs):
    for j, mHch in enumerate(mHchs):
        if not ((mH < mA) & (mA < mHch)):
            continue
        if mA - mH > 80:
            continue
        
        print(f"{mH}, {mA}, {mHch}")
        run_name = f'{run_prefix}_mH{mH}_mA{mA}_mHch{mHch}'
        run_directory = f"{base_dir}/{run_prefix}/{run_name}"

        # Check if it already exists, if it does skip it
        if os.path.isdir(run_directory):
            continue

        try:
            os.mkdir(run_directory)
        except:
            pass


        for template_filename in files:
            file = readFile(template_filename)

            file = replaceInFile(file, defines, process, run_name, mH, mA, mHch)

            filename = f'{run_name}{template_filename}'
            file_dir = f'{run_directory}/{filename}'
            saveFile(file, file_dir)
        
        
        with open(f"{base_dir}/input_arguments.txt", "a") as f:
            f.write(f"{mH}, {mA}, {mHch}\n")

   
