#!/afs/cern.ch/user/e/ecurtis/miniconda3/envs/idm/bin/python
import subprocess
import sys
import os.path

mH, mA, mHch, process, base_dir = sys.argv[1], sys.argv[2], sys.argv[3], str(sys.argv[4]), str(sys.argv[5])
print(f"mH = {mH}, mA = {mA}, mHch = {mHch}")
print(f"Process = {process}")
print(f"Base directory = {base_dir}")


cmd = "ls"
print(f"Doing ls:")
status, out = subprocess.getstatusoutput(cmd)
print(out)


# First I need to untar the MG file
print('Untarring MG file')
cmd = "tar -xvzf MG5_aMC_v2_6_7_forCondor.tar.gz"
status, out = subprocess.getstatusoutput(cmd)
# Check that it exists
isMGfile = os.path.exists("MG5_aMC_v2_6_7/") 
print(f"Does MG directory exists? -> {isMGfile}")


# MadGraph dirdctory
MG_dir = "MG5_aMC_v2_6_7"


def getXS(particle):
    with open(f'cross_section_{particle}.txt', 'r') as f:
        xs_file = f.readlines()
    for line in xs_file:
        if line.startswith("run_01"):
            decay = float(line.split(" ")[2])
    return decay


# First I need to read in the set commands
with open(f'{process}_mH{mH}_mA{mA}_mHch{mHch}_customizecards.dat', 'r') as f:
    set_commands = f.read()
print(set_commands)

################################### h3 Width ########################################
# The first thing I want to do is code to create the MG txt script 
with open('find_h3_decay.txt', 'w') as f:
    f.write('import model InertDoublet_UFO\n')
    f.write('generate h3 > h2 all all\n')
    f.write(f'output {process}_h3Width\n')
    f.write(f'launch {process}_h3Width\n')
    # for line in set_commands:
    #     f.write(line)
    f.write(set_commands)
    f.write(f'launch {process}_h3Width -i\n')
    f.write('print_results --path=./cross_section_h3.txt --format=short\n')

# Now run this
cmd = f"python2 {MG_dir}/bin/mg5_aMC find_h3_decay.txt"
status, out = subprocess.getstatusoutput(cmd)
print(out)

# Now that I have the h3 decay, I can update the set commands
# First read what the xs is
h3_decay = getXS("h3")
print(f"h3 h3_decay = {h3_decay}")



################################### h+ Width ########################################
# Now repeat but for h+
# The first thing I want to do is code to create the MG txt script 
with open('find_hch_decay.txt', 'w') as f:
    f.write('import model InertDoublet_UFO\n')
    f.write('generate h+ > h2 all all\n')
    f.write(f'output {process}_hchWidth\n')
    f.write(f'launch {process}_hchWidth\n')
    # for line in set_commands:
    #     f.write(line)
    f.write(set_commands)
    f.write(f'launch {process}_hchWidth -i\n')
    f.write('print_results --path=./cross_section_hch.txt --format=short\n')

# Now run this
cmd = f"python2 {MG_dir}/bin/mg5_aMC find_hch_decay.txt"
status, out = subprocess.getstatusoutput(cmd)
print(out)


hch_decay = getXS("hch")
print(f"hch hch_decay = {hch_decay}")






################################### Update Widths ########################################
# Now replace and update the set commands
set_commands = set_commands.replace("set param_card DECAY 36 1.0000", f"set param_card DECAY 36 {h3_decay}")
set_commands = set_commands.replace("set param_card DECAY 37 1.0000", f"set param_card DECAY 37 {hch_decay}")


# Now overwrite the set commands
with open(f'{process}_mH{mH}_mA{mA}_mHch{mHch}_customizecards.dat', 'w') as f:
    f.write(set_commands)


# Now I copy it back to afs 
cmd = f"cp -f {process}_mH{mH}_mA{mA}_mHch{mHch}_customizecards.dat {base_dir}/{process}/{process}_mH{mH}_mA{mA}_mHch{mHch}/{process}_mH{mH}_mA{mA}_mHch{mHch}_customizecards.dat"
status, out = subprocess.getstatusoutput(cmd)