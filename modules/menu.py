from functions.menu_functions import *
import time
class Menu:
	def __init__(self,font, oled, drinks_data, led_controller, tensometer, pumps):
		print('Uruchomiono kontroler menu')
		self.led_controller = led_controller
		self.menu_state = 'startup'
		self.font = font
		self.oled = oled
		self.drinks_data = drinks_data
		self.drinks_list = []
		self.fill_list(self)
		fun_startup(self.oled)
		time.sleep(2)
		start_menu(self.font, self.oled)
		self.global_iterator = 0
		self.current_drink = ""
		self.tensometer = tensometer
		self.pumps = pumps

	def fill_list(self, x):
		iterator = 0
		for item in self.drinks_data['drinks']:
			temp = item['name']
			self.drinks_list.append(temp)

	def power_off(self):
		self.menu_state = 'power_off'
		fun_power_off(self.oled)

	def get_state(self):
		return self.menu_state

	def power_on(self):
		self.menu_state = 'startup'
		fun_power_on(self.font, self.oled)

	def choose_drink(self):
		self.menu_state = 'choosing_drink'

	def show_drink(self):
		if self.global_iterator == len(self.drinks_list):
			self.global_iterator = 0
		fun_change_drink(self.oled, self.font, self.drinks_list[self.global_iterator])
		print(self.drinks_list[self.global_iterator])
		self.current_drink = self.drinks_list[self.global_iterator]
		self.global_iterator = self.global_iterator +1

	def get_current_drink(self):
		return self.current_drink

	def make_drink(self):
		fun_making_drink(self.oled, self.font, self.current_drink)
		self.led_controller.working(self.current_drink.lower())
		self.led_controller.go_back()
		ingredients = self.drinks_data[self.current_drink.lower()]
		print("Wybrałem drinka")
		for alcohol in ingredients:
			for value in alcohol:
				if alcohol[value] != '0':
					glass = self.tensometer.get_weight()
					weight = 0
					#WŁĄCZYĆ POMPĘ
					self.pumps.pour(value)
					print(value)
					print(alcohol[value])
					#Ruszam pompę na tyle ml ile mi mówi alcohol[value]
					while  weight-glass < int(alcohol[value]):
						weight = self.tensometer.get_weight()
						print("glass : {} weight : {} weight-glass: {}".format(glass, weight, weight-glass))
						time.sleep(0.1)
					self.pumps.pump_off()
		#Można zrobić tutaj progress-bar. Zobaczymy.
		#Procedura nalewania
		#Zmiana na wyświetlaczu
		#światełka w pozycji jałowej
