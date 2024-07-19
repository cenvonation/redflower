#                                        M A D E  B Y  @stolefromcloudflare
# T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

import subprocess
import re

def get_fastboot_info():
    try:
        result = subprocess.run(['fastboot', 'getvar', 'all'], capture_output=True, text=True)
        output = result.stdout + result.stderr  # Include stderr in case output goes there

        if not output:
            print("No output from fastboot. Make sure the device is connected and in fastboot mode.")
            return

        partitions = re.findall(r'\(bootloader\) partition-(size|type):(\w+): (.+)', output)
        partition_info = {}
        for attr, name, value in partitions:
            if name not in partition_info:
                partition_info[name] = {}
            partition_info[name][attr] = value

        baseband_match = re.search(r'\(bootloader\) version-baseband: (.+)', output)
        baseband_version = baseband_match.group(1) if baseband_match else 'Unknown'

        imei_matches = re.findall(r'\(bootloader\) imei\w*: (.+)', output)
        imeis = imei_matches if imei_matches else ['null']

        print(f"{'Partition Name':<20} | {'Size':<20} | {'Type'}")
        print('_' * 60)
        for name, attrs in partition_info.items():
            size = attrs.get('size', 'Unknown')
            type_ = attrs.get('type', 'Unknown')
            print(f"{name:<20} | {size:<20} | {type_}")

        print(f"\nBaseband version: {baseband_version}")
        print(f"IMEI's: {', '.join(imeis)}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_fastboot_info()
