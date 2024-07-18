#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

# UNFINISHED !!!!!!!!!!!!!

import subprocess
import os
import time

os.chdir('bin')
os.chdir("aria2c")

dldir = os.path.exists("dl")

if dldir == True:
    print('Download Directory exists. Skipping...')
else:
    os.mkdir("dl")

dlprompt = input("""MIUITN Downloader

MIUI 13:
[1] MIUITN V2.3 13.0.6.0

MIUI 14
[2] MIUITN V2.2 14.0.3.0
[3] MIUITN V2.3 14.0.3.0

More ROM's can be found at t.me/redmi10_community

Option: """)
if dlprompt == "1":
    romdl = os.path.exists("dl\\rom.zip")

    if romdl == True:
        print('Rom has already been downloaded. Skipping...')
    else:
        print("Starting Download... Please be patient")

        tn13 = "aria2c -d dl -o rom.zip https://miuitn.online/d/MIUITN/Selene/Ver2.3/MIUITN_V2.3_Selene_13.0.6.0.STABLE_A12_04Jan24.zip"
        subprocess.Popen(tn13, shell=True)
    print("Finished. Run extracter at bin/aria2c/extract.py")
    time.sleep(5000)
elif dlprompt == "2":
    romdl = os.path.exists("dl\\rom.zip")

    if romdl == True:
        print('Rom has already been downloaded. Skipping...')
    else:
        print("Starting Download... Please be patient")

        tn142 = "aria2c -d dl -o rom.zip https://miuitn.online/d/MIUITN/Selene/Ver2.2/MIUITN_V2.2_Selene_14.0.3.0_A13_urm_11Nov23.zip"
        subprocess.Popen(tn142, shell=True)
    print("Finished. Run extracter at bin/aria2c/extract.py")
    time.sleep(5000)
elif dlprompt == "3":
    romdl = os.path.exists("dl\\rom.zip")

    if romdl == True:
        print('Rom has already been downloaded. Skipping...')
    else:
        print("Starting Download... Please be patient")

        tn143 = "aria2c -d dl -o rom.zip https://miuitn.online/d/MIUITN/Selene/Ver2.3/MIUITN_V2.3_Selene_14.0.3.0.STABLE_A13_03Jan24.zip"
        subprocess.Popen(tn143, shell=True)
    print("Finished. Run extracter at bin/aria2c/extract.py")
    time.sleep(5000)
else:
    print("Unknown command. Rerun script to restart?")



##############
#CODE ARCHIVE#
##############

#aria2c = r"bin\aria2c\aria2c.exe"
#
#print("filepath is ", aria2c)
#
#download = aria2c, " https://miuitn.online/d/MIUITN/Selene/Ver2.3/MIUITN_V2.3_Selene_13.0.6.0.STABLE_A12_04Jan24.zip"
#subprocess.Popen(download, shell=True)
