#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S



import subprocess
import os
import shutil
import zipfile

print("Starting")

##############
#CODE ARCHIVE#
##############

#adbprompt = input("Do you want to install platform_tools (recommended) [yes, no]: ")
#if adbprompt == "yes":
#    print("Starting Download... Please be patient")
#
#    os.chdir('bin')
#    os.chdir("aria2c")
#    shutil.rmtree("dl")
#    os.mkdir("dl")
#    adb = "aria2c -d dl https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
#    subprocess.Popen(adb, shell=True)
#    os.chdir("dl")
#    os.mkdir("extracted")
#    tar = "tar -xf platform-tools-latest-windows.zip -C extracted"
#elif adbprompt == "no":
#    print("Skipping...")
#else:
#    print("Unknown command. Rerun script to restart?")