#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

import subprocess

command = "cls"
subprocess.Popen(command, shell=True)
def get_device_info():
    try:
        os_version = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode().strip()
        vendor = subprocess.check_output(["adb", "shell", "getprop", "ro.product.manufacturer"]).decode().strip()
        model_name = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode().strip()
        serial_number = subprocess.check_output(["adb", "get-serialno"]).decode().strip()

        print("Found device: ")
        print(f"OS Version: Android {os_version}")
        print(f"Vendor: {vendor}")
        print(f"Model Name: {model_name}")
        print(f"Serial Number: {serial_number}")

    except subprocess.CalledProcessError as e:
        print("Uh oh! Error occured while obtaining device information:", e)

if __name__ == "__main__":
    get_device_info()


##############
#CODE ARCHIVE#
##############

## Show connections. Shows only SN in [] and shows nothing when disconnected ##

#import android_controller

#connections = android_controller.checkConnections()
#print("Showing Android connections. If none shown, enable USB debugging.")
#print(connections)