import subprocess
import os 
import time

process = "h2h2lPlMnunu"
mH = 70
cmd = "pwd"
status, work_dir = subprocess.getstatusoutput(cmd)


with open(f"mH{mH}/input_arguments.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]

for line in lines[:4]:
    mH = int(line.split(",")[0])
    mA = int(line.split(" ")[1].split(",")[0])
    mHch = int(line.split(" ")[-1])
    print(mH, mA, mHch)

    python_loc = "~/miniconda3/envs/higgs-dna/bin/python"
    log_loc = f"{work_dir}/logs/{process}_{mH}_{mA}_{mHch}.log"
    err_loc = f"{work_dir}/logs/{process}_{mH}_{mA}_{mHch}.err"
    base_dir = f"{work_dir}/mH{mH}/{process}"

    cmd = f"qsub -q hep.q -l h_rt=1800 -o {log_loc} -e {err_loc} qsub_run_in_folder.sh {mH} {mA} {mHch} {process} {base_dir}"
    print(cmd)
    status, out = subprocess.getstatusoutput(cmd)
    print(out)

    # Crashes otherwise, of fucking course
    time.sleep(7.5)