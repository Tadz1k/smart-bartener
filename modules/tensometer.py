import RPi.GPIO as GPIO
from hx711 import HX711


class Tensometer:
	def __init__(self):
		self.hx = HX711(7, 8)
		self.hx.set_reading_format("MSB", "MSB")
		self.hx.set_reference_unit(862)
		self.hx.tare()

	def power_up(self):
		self.hx.power_up()

	def power_down(self):
		self.hx.power_down()

	def tare(self):
		self.hx.tare()
		print("XD")

	def get_weight(self):
		self.hx.power_up()
		val = self.hx.get_weight(5)
		self.hx.power_down()
		if val > 0: 
			return val
		else:
			return val * -1
