#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

# UNFINISHED !!!!!!!!!!!!!

import subprocess
import os
import shutil

aria2c = r"bin\aria2c\aria2c.exe"

print("filepath is ", aria2c)

download = aria2c, " -d dl https://drive.google.com/uc?export=download&id=1UTaXmcKDA0hvws4tmlB_n_VuIgqN9a56&confirm=t"

subprocess.Popen(download, shell=True)
