import threading
import time

class Inactivity (threading.Thread):

	def __init__(self, menu, oled):
		print('Uruchomiono moduł bezczynnośći')
		threading.Thread.__init__(self)
		self.menu = menu
		self.oled = oled
		self.time = 0

	def reset_time(self):
		self.time = 0

	def run(self):
		while True:
			if self.time == 120:
				self.menu.power_off()
				while(self.menu.get_state() == 'power_off'):
					time.sleep(1)
					pass
				self.reset_time()
			self.time = self.time+1
			time.sleep(1)

