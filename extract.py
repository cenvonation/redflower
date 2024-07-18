#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

import subprocess
import os

exdir = os.path.exists("extracted")
romcheck = os.path.exists("rom.zip")
batcheck = os.path.exists("MiuiTN_Install_Fastboot.bat")

os.chdir("bin\\aria2c\\dl")
if romcheck == True:
    print("Rom zip exists. Skipping...")
    if exdir == True:
        print("Extract folder exists. Skipping...")
        os.chdir("extracted")
        if batcheck == True:
            subprocess.Popen(r'explorer /select,"MiuiTN_Install_Fastboot.py"')
            print("Installer is present. Attempting to run Installer.")
        else:
            print("Installer not found!?? Make sure name of the file is MiuiTN_Install_Fastboot.bat.")
    else:
        os.mkdir("extracted")
        os.chdir("extracted")
else:
    if exdir == True:
        print("Extract folder exists. Skipping...")
    else:
        os.mkdir("extracted")
    print("Extracting Rom. Check File explorer.")
    tar = "tar -xf rom.zip -C extracted"
    subprocess.Popen(tar, shell=True)
    subprocess.Popen('explorer "extracted"')