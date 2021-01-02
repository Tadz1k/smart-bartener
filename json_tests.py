import json
data = open('drinks/drinks.json',)
drinks = json.load(data)
for i in drinks['paradise_bay']:
	print(i)
data.close()
