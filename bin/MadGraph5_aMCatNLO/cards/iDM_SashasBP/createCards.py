import os
import numpy as np

# These are the custom parameters for the run
mH = 120

run_prefix = 'h2h2muPmuM'
# put a \n in between each line
defines = 'define l+ = e+ mu+ \ndefine l- = e- mu- \ndefine vl = ve vm vt \ndefine vl~ = ve~ vm~ vt~'
process = 'generate p p > h2 h2 mu+ mu-'
mA = 150
mH = 80
mHch = 193
lam345 = 0.0
lam2 = 5.000000e-04 * 2

# Now create the folder for it
os.makedirs(f"{run_prefix}", exist_ok = True)



files = ['_proc_card.dat', '_run_card.dat', '_customizecards.dat', '_extramodels.dat']

def replaceInFile(file, defines, process, run_name, mH, mA, mHch, lam2, lam345):
    file = file.replace("<DEFINE>", defines)
    file = file.replace("<PROCESS>", process)
    file = file.replace("<RUN_NAME>", run_name)
    file = file.replace("<MH2>", str(mH))
    file = file.replace("<MH3>", str(mA))
    file = file.replace("<MHPM>", str(mHch))
    file = file.replace("<LAM2>", str(lam2 / 2))
    file = file.replace("<LAML>", str(lam345 / 2))
    return file

def readFile(filename):
    with open(filename, 'r') as f:
        file = f.read()
    return file

def saveFile(file, filename):
    with open(filename, 'w') as f:
        f.write(file)




run_name = f'{run_prefix}'
run_directory = f"{run_prefix}"
try:
    os.mkdir(run_directory)
except:
    pass


for template_filename in files:
    file = readFile(template_filename)

    file = replaceInFile(file, defines, process, run_name, mH, mA, mHch, lam2, lam345)

    filename = f'{run_name}{template_filename}'
    file_dir = f'{run_directory}/{filename}'
    saveFile(file, file_dir)

   
