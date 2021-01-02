import board
import neopixel
import RPi.GPIO as GPIO
import time
import random

global_var = 'idle'

GPIO.setmode(GPIO.BCM)
pixels = neopixel.NeoPixel(
    board.D18, 8, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB
)
#Paradise bay
def paradise_bay():
	r = 10
	g = 10
	b = 140
	for numb in range(8):
		pixels[numb] = (g, r, b)
		g = g+25
		r = r+10
		b = b-10

#Kamikadze
def kamikadze():
	r = 9
	g = 0
	b = 255
	for numb in range(8):
		pixels[numb] = (g,r,b)
		g = g+32
		r = r-1
		b = b-8

#Zielona ropucha
def zielona_ropucha():
	r = 20
	g = 236
	b = 9
	for numb in range(8):
		pixels[numb] = (g,r,b)
		g = g-20
		r = r-2 
		b = b+33

#Whiskey sour
def whiskey_sour():
	r = 66
	g = 0
	b = 14
	for numb in range(8):
		pixels[numb] = (g,r,b)
		g = g+32
		r = r+26 
		b = b-1

#Whisky z colą
def whiskey_with_cola():
	r = 255
	g = 23
	b = 5
	for numb in range(8):
		pixels[numb] = (g,r,b)
		r = r-2
		g = g+29


#Whiting sunset
def whiting_sunset():
	r = 255
	g = 0
	b = 0
	for numb in range(8):
		pixels[numb] = (g,r,b)
		g = g+32
#paradise_bay()
#kamikadze()
#zielona_ropucha()
#whiskey_sour()
#whiskey_with_cola()
#whiting sunset
def fun_idle():
	global global_var
	for i in range(8):
		if global_var == 'idle':
			r = random.randint(1,254)
			g = random.randint(1,254)
			b = random.randint(1,254)
			pixels[i] = (g,r,b)
			time.sleep(1)
			show()


def set_var(text):
	global global_var
	global_var = text

def show():
	pixels.show()


