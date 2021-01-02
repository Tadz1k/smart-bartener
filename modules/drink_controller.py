import json

class Drinks:
	def __init__(self):
		self.drinks_data = open('drinks/drinks.json',)
		self.drinks = json.load(self.drinks_data)
		self.drinks_data.close()


	def get_drinks(self):
		return self.drinks
