import os
import numpy as np
import sys

run_prefix = 'h2h2lPlM'

# put a \n in between each line
defines = 'define l+ = e+ mu+ \ndefine l- = e- mu- \ndefine vl = ve vm vt \ndefine vl~ = ve~ vm~ vt~'
process = 'generate p p > h2 h2 l+ l-'

# define the mass splittings
mHs = np.arange(60, 120, 10)
mAs = np.arange(60, 200, 10)

base_dir = "cards"


# Check if directory already exists as we don't want to overwrite them 
# if the decays have already been found! 
if os.path.exists(f"{base_dir}"):
    print(f"Directory already exists, exiting so that it doesn't overwrite the decays that have been found!")
    sys.exit(0)
else:    
    os.makedirs(base_dir, exist_ok = True)






files = ['_proc_card.dat', '_run_card.dat', '_customizecards.dat', '_extramodels.dat']

def replaceInFile(file, defines, process, run_name, mH, mA):
    file = file.replace("<DEFINE>", defines)
    file = file.replace("<PROCESS>", process)
    file = file.replace("<RUN_NAME>", run_name)
    file = file.replace("<MH2>", str(mH))
    file = file.replace("<MH3>", str(mA))
    file = file.replace("<MHPM>", str(250))
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



for mH in mHs:
    for mA in mAs:
        if not ((mH < mA) & ((mA - mH) <= 80) & (mA - mH > 20)):
            continue

        print(f"{mH}, {mA}")
        run_name = f'{run_prefix}_mH{mH}_mA{mA}'
        run_directory = f"{base_dir}/mH{mH}/{run_name}"



        os.makedirs(run_directory, exist_ok=True)



        for template_filename in files:
            file = readFile(template_filename)

            file = replaceInFile(file, defines, process, run_name, mH, mA)

            filename = f'{run_name}{template_filename}'
            file_dir = f'{run_directory}/{filename}'
            saveFile(file, file_dir)
        
        
        with open(f"{base_dir}/input_arguments.txt", "a") as f:
            f.write(f"{mH}, {mA}\n")




   
