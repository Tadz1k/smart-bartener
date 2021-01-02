
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)

def start_menu(font, oled):
	global image
	global draw
	image = Image.new("1", (oled.width, oled.height))
	draw = ImageDraw.Draw(image)
	draw.text((0,0), "> Gotowe drinki", font=font, fill=255)
	draw.text((0,25), "> Stwórz drinka", font=font, fill=255)
	draw.text((45,50), "Odpowietrzanie <", font=font, fill=255)
	oled.image(image)
	oled.show()

def fun_power_off(oled):
	oled.fill(0)
	oled.show()
	print('Faza bezczynności - ekran wyłączony')

def fun_power_on(font, oled):
	global image
	global draw
	image = Image.new("1", (oled.width, oled.height))
	draw = ImageDraw.Draw(image)
	draw.text((0,0), "> Gotowe drinki", font=font, fill=255)
	draw.text((0,25), "> Stwórz drinka", font=font, fill=255)
	draw.text((45,50), "Odpowietrzanie <", font=font, fill=255)
	oled.image(image)
	oled.show()

def fun_startup(oled):
	global image
	global draw
	image = Image.new("1", (oled.width, oled.height))
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("/usr/share/fonts/truetype/openoffice/lato/Lato-Bold.ttf", 15)
	font2 = ImageFont.truetype("/usr/share/fonts/truetype/openoffice/dejavu/DejaVuSerif.ttf", 10)
	draw.text((20,0), "   SMART\nBARTENER", font=font, fill=255)
	draw.text((10, 50), " ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) ", font=font2, fill=255)
	oled.image(image)
	oled.show()

def fun_change_drink(oled, font, drink):
	global image
	global draw
	image = Image.new("1", (oled.width, oled.height))
	draw = ImageDraw.Draw(image)
	font2 = ImageFont.truetype("/usr/share/fonts/truetype/openoffice/lato/Lato-Bold.ttf", 15)
	draw.text((15, 24), drink, font=font2, fill=255)
	draw.text((0, 0), '<cofnij', font=font, fill=255)
	draw.text((100, 0), 'dalej>', font=font, fill=255)
	draw.text((50,50), '!LEJ!', font=font, fill=255)
	oled.image(image)
	oled.show()

def fun_making_drink(oled, font, drink):
	global image
	global draw
	image = Image.new("1", (oled.width, oled.height))
	draw = ImageDraw.Draw(image)
	font2 = ImageFont.truetype("/usr/share/fonts/truetype/openoffice/lato/Lato-Bold.ttf", 20)
	draw.text((50, 0), "Trwa nalewanie...", font=font, fill=255)
	draw.text((15, 20), drink, font=font2, fill=255)
	oled.image(image)
	oled.show()
