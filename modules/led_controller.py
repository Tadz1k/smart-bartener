import threading
import time
import board
import neopixel
import RPi.GPIO as GPIO
import random
from functions.led_functions import *

class Led (threading.Thread):
	def __init__(self):
		print('Uruchomiono moduł LED')
		threading.Thread.__init__(self)
		self.state = 'idle'
		self.idle_set = False

	def run(self):
		print('ruszylem')
		while True:
			if self.state == 'idle':
				fun_idle()
				time.sleep(0.2)
			time.sleep(0.2)

	def working(self, drink):
		print(drink)
		set_var('working')
		self.state = 'working'
		if drink == 'paradise bay':
			paradise_bay()
			show()
		if drink == 'kamikadze':
			print('Leję kamikadze!')
			kamikadze()
			show()
		if drink == 'zielona ropucha':
			zielona_ropucha()
			show()
		if drink == 'whiskey sour':
			whiskey_sour()
			show()
		if drink == 'whiskey z colą':
			whiskey_with_cola()
			show()
		if drink == 'whiting sunset':
			whiting_sunset()
			show()

	def go_back(self):
		self.state = 'idle'
		set_var('idle')

