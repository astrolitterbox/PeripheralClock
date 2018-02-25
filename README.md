# Persistence of vision LED wall clock

Based on Science Hack Day Vilnius 2018 participant badge code by _miceuz_ (https://github.com/Technariumas/shd18badge) and Adafruit bitmapfont.py library.

## Prerequisites

To program WEMOS D1, you will need the following:

 * A laptop with Linux, Mac OS or Windows and at least one free USB port.
 * If it’s Windows or Mac OS, make sure to install [drivers](https://wiki.wemos.cc/downloads) for the CH340 UBS2TTL chip.
 * A micro-USB cable with data lines that fits your USB port.
 * You will need a terminal application installed. For Linux and Mac you can use screen, which is installed by default. For Windows we recommend [PuTTy](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) or [CoolTerm](http://freeware.the-meiers.org/).
 
## Programming

Use dmesg to determine the USB port ([usb]) the badge is connected to, e.g. /dev/ttyUSB0.

Flash the firmware:
cd shd18badge/micropython

Edit the flash_microcontroller.sh file so that it points to the correct USB port. If esptool.py is needed, install it (for example, pip install esptool.py). Then copy the files to the microcontroller:

python transfer_files.py -p /dev/[usb] -b 115200 util.py main.py boot.py
 
## Tutorial
 * A pretty great [tutorial is available here](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/index.html)
 * [A MAC user first hand experience](MACUSERS.md) using the SHD badge
