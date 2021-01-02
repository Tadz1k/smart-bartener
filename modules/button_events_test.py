import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def pressed_19(channel):
	print('Pressed 19')

def pressed_13(channel):
	print('Pressed 13')

def pressed_21(channel):
	print('Pressed 21')

def pressed_20(channel):
	print('Pressed20')

def confirm(channel):
	print('Confirmed')


GPIO.setwarnings(False)
#Puszczam stale prąd na pin BCM.26 - zasilam taśmę '+'
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 1)

#Przyciski
#19		13
#21		20
#       16
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(19, GPIO.RISING, callback = pressed_19, bouncetime=300)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(13, GPIO.RISING, callback = pressed_13, bouncetime=300)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(21, GPIO.RISING, callback = pressed_21, bouncetime=300)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(20, GPIO.RISING, callback = pressed_20, bouncetime=300)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(16, GPIO.RISING, callback = confirm, bouncetime=300)

message=input('press enter');
GPIO.cleanup()
