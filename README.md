# Red Flower
## !!!THIS TOOL IS STILL UNFINISHED DONT USE IT YET!!!
A multipurpose tool for the Redmi 10/Prime/Note 11 4G 

(This project can be used on any other device actually but it's mostly dedicated to use on the selene/selenes model of Redmi devices.)

# Stuff used:
### platform-tools by Google
### aria2c by aria2

#### Disclamer #1:
This project is my biggest one yet and it may be super simple but for me, making something like this makes me proud.

#### Disclaimer #2:
This project has code archives in some files which is basically just old bits of code that I decided to remake and store them somewhere if I would need them again in the near future.

#### Currently supported OS is Windows. Other OS support will soon arrive to:
- MacOS
- Linux (limited)
- Possibly Android with Termux terminal emulator

#### Red Flower Features Checklist:
- Track Android logcat [**FINISHED**]
- Show device information [**FINISHED**]
- Download/flash custom MIUI [**FINISHED**]
- Flash GSI [**FINISHED**]
- Flash custom recoveries (TWRP, OFOX) [**FINISHED**]
- Manage packages (Apps/APK) [**WORK REQUIRED**]
- Reboot menus ADB and FASTBOOT [**FINISHED**]
- List partitions name, size, type + show baseband version and IMEI's [**FINISHED**]
- Separate partition flashing [**FINISHED**]
~~- Backup IMEI (nvram, nvdata for custom rom) [NOT STARTED YET]~~ **READ NOTES**
- Fix dm-verity error on boot [**FINISHED**]

## NOTES

PACKAGEMGR.PY INSTALL/UNINSTALL DOESNT WORK ON MY END AND PROBABLY WILL NOT ON YOURS TOO. UNTIL THEN WAIT FOR A FIX.

BACKING UP IMEI WILL NOT BE A THING FOR A BIT UNTIL I FIGURE OUT HOW TO EVEN DO IT

REMOVED NVDATA ERROR RESISTOR REMOVE FIX BECAUSE WHY MAKE A DEDICATED PYTHON FILE FOR SOMETHING LIKE THAT? (I will make a website where it's about Redmi 10/Prime/Note 11 4G tips, fixes, custom roms and tools and will include it there.)

## How to use

Clone the repo with git, cd into it and take a look at the different files you can run with Python and Batch
`git clone https://github.com/25freepb/redflower && cd redflower && dir *.py *.bat /S`

that's basically it lol

## Explaining each

### Python files

#### backup.py (see notes above)
Backs up your partitions holding the IMEI's. Useful for custom roms and accidental Format all + Download in SP Flash Tool.

#### deviceinfo.py
Shows your OS version, vendor, model name and SN.

#### dmverity-fix.py
Fixes the dmverity error on boot if it appears before the bootlogo.

#### download.py
Let's you download custom MIUI versions for the selene/selenes model. Stores it in `redflower/bin/aria2c/dl/`.

#### extract.py
Extracts an existing custom MIUI rom downloaded with `download.py`. Python will error if `rom.zip` doesn't exist in `redflower/bin/aria2c/dl/`.

#### logcat.py
Let's you run a logcat of your system while connected to the PC. Ctrl + C or unplug from PC to stop.

#### packagemgr.py
View installed apps, install apps from your PC and uninstall apps. Still needs some work but it's usable to an extent.

#### partitions.py
List's the partition name, size and type while in fastboot mode. Also shows baseband version and IMEI 1 and 2.

#### reboot-adb.py and reboot-fastboot.py
Let's you reboot your phone in different modes from either adb or fastboot. Scripts located in `redflower/reboot/`.

### Batch files

#### Flashing partition.bat and recovery.bat
Partition.bat let's you flash a specific partition with your image file to drag in the Terminal window. Recovery.bat let's you flash TWRP or OFOX images to the boot slot and automatically reboot to it.

#### GSI Install.bat
Let's you automate the install of a ARM64 A/B GSI image on your device. Read `READ FIRST.md` located in `redflower/gsi/` before coninuing

**Thank you!!!** for using my project! Again, this is my first major project and things are janky but I will try my best to improve it by a lot.

Thanks again!

https://t.me/Redmi10_Community

TG @stolefromcloudflare
