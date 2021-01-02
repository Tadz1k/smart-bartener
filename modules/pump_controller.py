import board
import RPi.GPIO as GPIO
import time
class Pumps:
	def __init__(self):
	#Spis pomp
		print('Uruchomiono moduł pomp')
		GPIO.setup(12, GPIO.OUT)
		GPIO.setup(25, GPIO.OUT)
		GPIO.setup(24, GPIO.OUT)
		GPIO.setup(23, GPIO.OUT)
		GPIO.setup(17, GPIO.OUT)
		GPIO.setup(27, GPIO.OUT)
		GPIO.setup(22, GPIO.OUT)
		GPIO.setup(2, GPIO.OUT)
		GPIO.output(12, 0)
		GPIO.output(25, 0)
		GPIO.output(24, 0)
		GPIO.output(23, 0)
		GPIO.output(17, 0)
		GPIO.output(27, 0)
		GPIO.output(22, 0)
		GPIO.output(2, 0)
		self.current_pump = -1


	def pour(self, item):
		if item == 'cola':
			self.current_pump = 12
		if item == 'whiskey':
			self.current_pump = 25
		if item == 'lemon':
			self.current_pump = 24
		if item == 'white_vodka':
			self.current_pump = 23
		if item == 'blue_curacao':
			self.current_pump = 17
		if item == 'grenadine':
			self.current_pump = 27
		if item == 'white_rum':
			self.current_pump = 22
		if item == 'orange':
			self.current_pump = 2
		self.pump_on()

	def pump_on(self):
		GPIO.output(self.current_pump, 1)

	def pump_off(self):
		GPIO.output(self.current_pump, 0)
		current_pump = -1
