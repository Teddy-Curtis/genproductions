import glob
mH = 80
process = "h2h2lll"


files = glob.glob(f"mH{mH}/{process}/*/*cards.dat")

print(files)

for file in files:
    mass_point = file.split("/")[-2]
    with open(file, "r") as f:
        info = f.read()
        
    #print(info)
    if "1.00" in info:

        print(f"Cards failed for: {mass_point}")