import sys
sys.path.append("./usr/local/lib/python3.9/dist-packages")
import usb.core
import board
import neopixel
import time

NUMBER_OF_LIGHTS = 251
WHITE = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(board.D18, NUMBER_OF_LIGHTS)

while True:
	pixels.fill(RED)
	time.sleep(0.333)
	pixels.fill(GREEN)
	time.sleep(0.333)
	pixels.fill(BLUE)
	time.sleep(0.333)
