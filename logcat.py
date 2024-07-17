#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

import subprocess

clear = "cls"
subprocess.Popen(clear, shell=True)

print("Starting logcat. Do not disconnect device for logcat to remain running. Ctrl + C to exit logcat.")

log = "adb logcat"
subprocess.Popen(log, shell=True)