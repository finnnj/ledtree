import board
import neopixel


NUM_PIXELS = 200
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness=0.6, auto_write=False)
