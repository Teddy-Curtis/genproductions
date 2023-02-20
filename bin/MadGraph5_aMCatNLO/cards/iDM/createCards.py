import os

# These are the custom parameters for the run
run_prefix = 'h2h2lPlM_lem'
# put a \n in between each line
defines = 'define l+ = e+ mu+ \ndefine l- = e- mu-'
process = 'p p > h2 h2 l+ l-'

# Now create the folder for it
try:
    os.mkdir(run_prefix)
except:
    pass


# Params in the form: MH, MA, MHPM, Lam2, Lam345
BP_params = [[72.77, 107.803, 114.639, 1.44513, -0.00440723], 
                      [65, 71.525, 112.85, 0.779115, 0.0004], 
                          [67.07, 73.222, 96.73, 0, 0.00738], 
             [73.68, 100.112, 145.728, 2.08602, -0.00440723], 
              [72.14, 109.548, 154.761, 0.0125664, -0.00234], 
                  [76.55, 134.563, 174.367, 1.94779, 0.0044], 
                  [70.91, 148.664, 175.89, 0.439823, 0.0058], 
                    [56.78, 166.22, 178.24, 0.502655, 0.00338], 
                  [76.69, 154.579, 163.045, 3.92071, 0.0096],
                   [58.31, 171.148, 172.96, 0.540354, 0.00762], 
                  [99.65, 138.484, 181.321, 2.46301, 0.0532], 
                 [71.03, 165.604, 175.971, 0.339292, 0.00596],
                   [71.03, 217.656, 218.738, 0.766549, 0.00214], 
                   [71.33, 203.796, 229.092, 1.03044, -0.00122], 
                     [147, 194.647, 197.403, 0.387, -0.018], 
                   [165.8, 190.082, 195.999, 2.7675, -0.004], 
                    [191.8, 198.376, 199.721, 1.5075, 0.008], 
             [57.475, 288.031, 299.536, 0.929911, 0.00192], 
               [71.42, 247.224, 258.382, 1.04301, -0.0032],
                    [62.69, 162.397, 190.822, 2.63894, 0.0056]]

files = ['_proc_card.dat', '_run_card.dat', '_customizecards.dat', '_extramodels.dat']

def replaceInFile(file, defines, process, run_name, params):
    file = file.replace("<DEFINE>", defines)
    file = file.replace("<PROCESS>", process)
    file = file.replace("<RUN_NAME>", run_name)
    file = file.replace("<MH2>", str(params[0]))
    file = file.replace("<MH3>", str(params[1]))
    file = file.replace("<MHPM>", str(params[2]))
    file = file.replace("<LAM2>", str(params[3]/2))
    file = file.replace("<LAML>", str(params[4]/2))
    return file

def readFile(filename):
    with open(filename, 'r') as f:
        file = f.read()
    return file

def saveFile(file, filename):
    with open(filename, 'w') as f:
        f.write(file)


for BP_num, params in enumerate(BP_params):
    BP_num += 1
    print(f'BP = {BP_num}')
    run_name = f'{run_prefix}_BP{BP_num}'
    run_directory = f"{run_prefix}/{run_name}"
    try:
        os.mkdir(run_directory)
    except:
        pass

    for template_filename in files:
        file = readFile(template_filename)

        file = replaceInFile(file, defines, process, run_name, params)

        filename = f'{run_name}{template_filename}'
        file_dir = f'{run_directory}/{filename}'
        saveFile(file, file_dir)
    
