#include <Adafruit_NeoPixel.h>
 
from machine import Pin, SPI, ADC
from neopixel import NeoPixel
from time import sleep 
import urandom
import util 
import ustruct

leds = 8
width = 15

pixel = NeoPixel(Pin(14, Pin.OUT), leds) #D5
dimFactor = 4
num = "32"
color = urandom.getrandbits(8)
font_name='font5x8.bin'
fontFile = open(font_name, 'rb')
font_width, font_height = (5, 8)
 

def draw_char(ch):
       # Go through each column of the character.
        for pos in range(font_width):
			draw_char_line(ch, pos)
			

def draw_char_line(ch, pos):
            # Grab the byte for the current column of font data.
            fontFile.seek(2 + (ord(ch) * font_width) + pos)
            line = ustruct.unpack('B', fontFile.read(1))[0]
            # Go through each row in the column byte.
            for y_pos in range(font_height):
                # Draw a pixel for each bit that's flipped on.
                if (line >> y_pos) & 0x1:
					pixel[y_pos] = [0, 32, 64]
            pixel.write()
            sleep(0.005)
            setPixels(0, 0, 0)


  
def setPixels(r, g, b):
	for n in range(leds):
		pixel[n] = [r, g, b]
	pixel.write() 

while True:
	[r, g, b] = util.colorWheel(color)
	#setPixels(r%dimFactor, g%dimFactor, b%dimFactor)
	#sleep(0.04)
	#draw_char("X")
	#sleep(10)
	#setPixels(0, 0, 0)
	#sleep(1)
	
