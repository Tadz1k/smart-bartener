import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
 
# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)
 
# Change these to the right size for your display!
WIDTH = 128
HEIGHT = 64 # Change to 64 if needed BORDER = 5
 
# Use for I2C. i2c = board.I2C() oled = 
#adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, 
#reset=oled_reset)
 
# Use for SPI
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D5)
oled_dc = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)
 
# Clear display.
oled.fill(0)
oled.show()
