::                                        M A D E  B Y  @stolefromcloudflare
:: T . M E / R E D M I 1 0 _ C O M M U N I T Y  |  T . M E / R E D M I 1 0 _ U P D A T E S  |  T . M E / R 1 0 R O M S

@echo off

echo REBOOT YOUR PHONE IN FASTBOOT/FASTBOOTD TO START FLASHING
TIMEOUT /T 1

set /p img="Drag Android partition image in Terminal window here: "
set /p part="Input partition name to flash (optional: include slot letter): "

echo Flashing to partition: %part%
fastboot flash %part% %img%

echo Finished.
TIMEOUT /T 3