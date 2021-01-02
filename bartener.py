"""
This demo will fill the screen with white, draw a black box on top
and then print Hello World! in the center of the display
 
This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!
"""
 
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
import RPi.GPIO as GPIO

from modules.controller import Controller

GPIO.setmode(GPIO.BCM)

font = ImageFont.truetype("/usr/share/fonts/truetype/quicksand/Quicksand-Bold.ttf", 10)


oled_reset = digitalio.DigitalInOut(board.D4)


WIDTH = 128
HEIGHT = 64
BORDER = 5
 

spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D5)
oled_dc = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)
 
oled.fill(0)
oled.show()
 
controller = Controller(font, oled)
#oled.image(image)
#oled.show()
