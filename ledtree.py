import time
import board
import random
import colorsys
import neopixel


class LEDTree:
    def __init__(self, num_pixels=200):
        self.pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.6, auto_write=False, pixel_order=neopixel.RGBW)


    def fill(self, red, green, blue, white):
        self.pixels.fill((red, green, blue, white))
        self.pixels.show()


    def randfill(self):
        self.fill(255, 0, 0, 0)
