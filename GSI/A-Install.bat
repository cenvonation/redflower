@echo off

echo Disabling verification
fastboot --disable-verification flash vbmeta Images\vbmeta.img
TIMEOUT /T 3

echo Installing GSI on AB device
fastboot reboot fastboot
echo Erasing system
fastboot erase system
TIMEOUT /T 3

echo Deleting product partiton
fastboot delete-logical-partition product
TIMEOUT /T 3

echo Flashing system. Please be patient...
fastboot flash system Images\system.img

echo Finished. Format data from recovery and reboot.
fastboot reboot recovery

echo Process ended
TIMEOUT /T 30