import os
import numpy as np

# These are the custom parameters for the run
mH = 120
base_dir = f"mH{mH}"
run_prefix = 'h2h2lPlM'
# put a \n in between each line
defines = 'define l+ = e+ mu+ \ndefine l- = e- mu- \ndefine vl = ve vm vt \ndefine vl~ = ve~ vm~ vt~'
process = 'generate p p > h2 h2 l+ l-'


mAs = np.arange(mH, mH + 120, 10)
mHchs = np.arange(mH, mH + 120, 10)


# Now create the folder for it
os.makedirs(f"{base_dir}/{run_prefix}", exist_ok = True)



files = ['_proc_card.dat', '_run_card.dat', '_customizecards.dat', '_extramodels.dat']

def replaceInFile(file, defines, process, run_name, mH, mA, mHch):
    file = file.replace("<DEFINE>", defines)
    file = file.replace("<PROCESS>", process)
    file = file.replace("<RUN_NAME>", run_name)
    file = file.replace("<MH2>", str(mH))
    file = file.replace("<MH3>", str(mA))
    file = file.replace("<MHPM>", str(mHch))
    file = file.replace("<LAM2>", str(0))
    file = file.replace("<LAML>", str(0.0000001))
    return file

def readFile(filename):
    with open(filename, 'r') as f:
        file = f.read()
    return file

def saveFile(file, filename):
    with open(filename, 'w') as f:
        f.write(file)




for mA in mAs:
    for mHch in mHchs:
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


        for template_filename in files:
            file = readFile(template_filename)

            file = replaceInFile(file, defines, process, run_name, mH, mA, mHch)

            filename = f'{run_name}{template_filename}'
            file_dir = f'{run_directory}/{filename}'
            saveFile(file, file_dir)

        # Also want to write inputs to a txt file
        with open(f"{base_dir}/input_arguments.txt", "a") as f:
            f.write(f"{mH}, {mA}, {mHch}\n")

   
