import RPi.GPIO as GPIO
from hx711 import HX711
import board
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.IN)
hx711 = HX711(7, 8, 128)
hx711.power_up()
hx711.reset()
measures = hx711.get_raw_data(3)
hx711.reset()
test = hx711.read(3)
print(test)
print(measures)
sum = 0
for weight in measures:
	sum = sum + weight
sum = sum/3
print(sum)
hx711.power_down()
