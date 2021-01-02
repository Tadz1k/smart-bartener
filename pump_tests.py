
import board
import RPi.GPIO as GPIO
import time

def zero(pumps_gpio):
	iterator = -1
	for pump in pumps_gpio:
		iterator = iterator + 1
		GPIO.output(pumps_gpio[iterator], 0)
imput = ""
pumps = [0,0,0,0,0,0,0,0]
pumps_gpio = [12,25,24,23,17,27,22,2]
iterator = -1
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)
zero(pumps_gpio)
#while imput != 'koniec':
#	zero(pumps_gpio)
#	print('podaj cyfre od 0 do 7')
#	imput = input()
#	pumps[int(imput)] = 1
#	GPIO.output(pumps_gpio[int(imput)], 1)
GPIO.output(pumps_gpio[0], 0)

GPIO.output(pumps_gpio[1], 0)

GPIO.output(pumps_gpio[2], 0)

GPIO.output(pumps_gpio[3], 0)

GPIO.output(pumps_gpio[4], 0)

GPIO.output(pumps_gpio[5], 0)

GPIO.output(pumps_gpio[6], 0)

GPIO.output(pumps_gpio[7], 0)

