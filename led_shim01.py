# Code test for Pimoroni's LED Shim

import ledshim
import time

ledshim.set_clear_on_exit()

'''
CONSTANTS
ledshim.NUM_PIXELS
ledshim.DISPLAY_WIDTH # Same as NUM_PIXELS?

FUNCTIONS
ledshim.clear()
ledshim.set_brightness(0.6)
ledshim.set_pixel(0,0,0,0)
ledshim.show()
'''

'''
#Pimoroni test.py code

for col in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
    r, g, b = col
    for x in range(ledshim.DISPLAY_WIDTH):
        ledshim.clear()
        ledshim.set_pixel(x, r, g, b)
        ledshim.show()
        time.sleep(0.2)
'''
