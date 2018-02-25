#include <Adafruit_NeoPixel.h>
 
from machine import Pin, SPI, ADC
from neopixel import NeoPixel
from time import sleep 
import urandom
import util 
import bitmapFont

leds = 8
pixel = NeoPixel(Pin(14, Pin.OUT), leds) #D5
dimFactor = 4
num = "32"
color = urandom.getrandbits(8)

  
def setPixels(r, g, b):
	for n in range(leds):
		pixel[n] = [r, g, b]
	pixel.write() 

while True:
	[r, g, b] = util.colorWheel(color)
	setPixels(r%dimFactor, g%dimFactor, b%dimFactor)
	sleep(0.04)
	setPixels(0, 0, 0)
	sleep(1)
	
