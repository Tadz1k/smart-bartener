from modules.menu import Menu
from modules.button_events import button_thread
from modules.inactivity import Inactivity
from modules.drink_controller import Drinks
from modules.led_controller import Led
from modules.pump_controller import Pumps
from modules.tensometer import Tensometer
import time
class Controller:
	def __init__(self, font, oled):
		print('Uruchomiono główny kontroller')
		self.font = font
		self.oled = oled
		self.led = Led()
		self.led.start()
		self.drinks_controller = Drinks()
		self.drinks_data = self.drinks_controller.get_drinks()
		self.tensometer = Tensometer()
		self.pumps = Pumps()
		self.menu = Menu(font, oled, self.drinks_data, self.led, self.tensometer, self.pumps)
		time.sleep(0.2)
		self.events_thread = button_thread(self.menu)
		self.events_thread.start()
		time.sleep(0.2)
		self.inactivity_controller = Inactivity(self.menu, self.oled)
		self.inactivity_controller.start()

