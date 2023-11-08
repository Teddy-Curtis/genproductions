# This just changes the run card for each point
# These are the custom parameters for the run
import os
import numpy as np
import sys

procs = ["h2h2lPlM", "h2h2lPlMnunu"]

mH = 80
base_dir = f"mH{mH}_new_run_card"

mAs = np.arange(mH, mH + 120, 10)
mHchs = np.arange(mH, mH + 120, 10)

def readFile(filename):
    with open(filename, 'r') as f:
        file = f.read()
    return file


def saveFile(file, filename):
    with open(filename, 'w') as f:
        f.write(file)

for proc in procs:
    for i, mA in enumerate(mAs):
        for j, mHch in enumerate(mHchs):
            if not ((mH < mA) & (mA < mHch)):
                continue
            if mA - mH > 80:
                continue
            
            print(f"{mH}, {mA}, {mHch}")
            run_name = f'{proc}_mH{mH}_mA{mA}_mHch{mHch}'
            run_directory = f"{base_dir}/{proc}/{run_name}"

            file = readFile("_run_card.dat")

            filename = f'{run_name}_run_card.dat'
            file_dir = f'{run_directory}/{filename}'
            saveFile(file, file_dir)