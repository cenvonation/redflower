#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

#https://dl.google.com/android/repository/platform-tools-latest-windows.zip

import subprocess

print("Starting")
adbprompt = input("Do you want to install platform_tools (recommended) [yes, no]: ")
if adbprompt == "yes":
    aria = "cd bin"
    dir = "dir"
    print("Starting Download... Please be patient")

    subprocess.Popen(aria, shell=True)
    subprocess.Popen(dir, shell=True)
elif adbprompt == "no":
    print("Skipping...")
else:
    print("Unknown command. Rerun script to restart?")