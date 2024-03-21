import subprocess
import os 
import time

process = "idm_dilepton"

cmd = "pwd"
status, work_dir = subprocess.getstatusoutput(cmd)


with open("cards/input_arguments.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]

for line in lines:
    mH = int(line.split(",")[0])
    mA = int(line.split(" ")[1])
    print(mH, mA)

    python_loc = "~/miniconda3/envs/higgs-dna/bin/python"
    log_loc = f"{work_dir}/logs/{mH}_{mA}.log"
    err_loc = f"{work_dir}/logs/{mH}_{mA}.err"
    base_dir = f"{work_dir}/cards/mH{mH}"

    cmd = f"qsub -q hep.q -l h_rt=1800 -o {log_loc} -e {err_loc} qsub_run_in_folder.sh {mH} {mA} {process} {base_dir}"
    print(cmd)
    status, out = subprocess.getstatusoutput(cmd)
    print(out)
    break 
    # Crashes otherwise, of fucking course
    time.sleep(5)