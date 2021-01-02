import RPi.GPIO as GPIO
import threading
from modules.menu import Menu
import time

class button_thread (threading.Thread):

	def __init__(self, menu):
		print('Uruchomiono wątek nasłuchu przycisków')
		threading.Thread.__init__(self)
		self.menu = menu

	GPIO.setmode(GPIO.BCM)

	def pressed_19(self, channel):
		if self.menu.get_state() == 'choosing_drink':
			self.menu.show_drink()


	def pressed_13(self):
		print('Pressed 13')

	def pressed_21(self):
		print('Pressed 21')

	def pressed_20(self, channel):
		if self.menu.get_state() == 'choosing_drink':
			print('powrot')
			self.menu.power_on() #Powrót do 'jałowej' pozycji
			return


		if self.menu.get_state() == 'startup':
			print('wybieram')
			self.menu.choose_drink()
			self.menu.show_drink()
			time.sleep(0.2)


	def confirm(self, channel):
		if self.menu.get_state() == 'choosing_drink':
			self.menu.make_drink()
		#Jeśli jest stan bezczynności
		if self.menu.get_state() == 'power_off':
			print('Włączam ekran po bezczynności')
			self.menu.power_on()
		print('Confirmed')


	GPIO.setwarnings(False)
	#Puszczam stale prąd na pin BCM.26 - zasilam taśmę '+'
	GPIO.setup(26, GPIO.OUT)
	GPIO.output(26, 1)

	#Przyciski
	#19		13
	#21		20
	#       16
	def run(self):
		GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		#GPIO.add_event_detect(19, GPIO.RISING, callback = self.pressed_19, bouncetime=300)

		GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		#GPIO.add_event_detect(13, GPIO.RISING, callback = self.pressed_13, bouncetime=300)

		GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		#GPIO.add_event_detect(21, GPIO.RISING, callback = self.pressed_21, bouncetime=300)

		GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		#GPIO.add_event_detect(20, GPIO.RISING, callback = self.pressed_20, bouncetime=300)

		GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		#GPIO.add_event_detect(16, GPIO.RISING, callback = self.confirm, bouncetime=300)
		#message = input('press enter to stop thread')	
		while True:
			if GPIO.input(19) == GPIO.HIGH:
				print('19')
				self.pressed_19(self)
				time.sleep(0.5)
			if GPIO.input(13) == True:
				print('13')
				time.sleep(0.5)
			if GPIO.input(21) == True:
				print('21')
				time.sleep(0.5)
			if GPIO.input(20) == True:
				print('20')
				self.pressed_20(self)
				time.sleep(0.5)
			if GPIO.input(16) == False:
				print('16')
				self.confirm(self)
				time.sleep(0.5)
			time.sleep(0.1)
		message=input('press enter');
		GPIO.cleanup()
