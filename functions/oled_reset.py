import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pixels = neopixel.NeoPixel(
    board.D18, 8, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB
)
pixels[0] = (0, 0, 0)
pixels.show()

