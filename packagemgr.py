#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

import subprocess
import tkinter as tk
from tkinter import filedialog
import time

pkg = input("""Options:
[v] View Installed Packages
[i] Install APK (doesnt work on my end)
[u] Uninstall Package (doesnt work on my end)

Option: """)
if pkg == "v":
    lp = "adb shell pm list packages"
    subprocess.Popen(lp, shell=True)
elif pkg == "i":
    apkd = tk.Tk()
    apkd.withdraw()

    apkp = filedialog.askopenfilename()
    confi = input("Are you sure to install? [y/n]:")
    if confi == "y":
        install = 'adb -e install ', apkp
        subprocess.Popen(install, shell=True)
    else:
        print("Aborting Install.")
elif pkg == "u":
    pkgn = input("Enter full package name: ")
    confu = input("Are you sure to uninstall? [y/n]:")
    if confu == "y":
        uninstall = "adb uninstall ", pkgn
        subprocess.Popen(uninstall, shell=True)
    else:
        print("Aborting Uninstall.")
else:
    print("Unknown command. Rerun script to restart?")

print("Finished.")