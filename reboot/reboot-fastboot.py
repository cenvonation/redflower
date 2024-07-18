#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

import subprocess

reboot = input("Reboot where? [system/recovery/bootloader/fastboot]: ")
if reboot == "system":
    sysr = "fastboot reboot"
    subprocess.Popen(sysr, shell=True)
elif reboot == "recovery":
    sysr = "fastboot reboot recovery"
    subprocess.Popen(sysr, shell=True)
elif reboot == "bootloader":
    sysr = "fastboot reboot bootloader"
    subprocess.Popen(sysr, shell=True)
elif reboot == "fastboot":
    sysr = "fastboot reboot fastboot"
    subprocess.Popen(sysr, shell=True)
else:
    print("Unknown Command. Rerun script to restart.")