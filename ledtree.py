import time
import board
import random
import colorsys
import neopixel


class LEDTree:
    def __init__(self, num_pixels=200):
        self.pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.6, auto_write=False)


    def fill(self, hue, sat, val):
        rgb = colorsys.hsv_to_rgb(hue, sat, val)
        self.pixels.fill(rgb)


    def randfill(self):
        self.pixels.fill(random.random(), random.random(), random.random())
