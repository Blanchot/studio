# Code test for Pimoroni's LED Shim

import ledshim
import time

ledshim.set_clear_on_exit()

rise = (0,255,0)
fall = (255,0,0)
same = (0,0,255)

print('Try: fallWalk(), riseWalk(), sameWalk()')

def reset():
  ledshim.clear()
  ledshim.show()

def fallWalk():
  for x in range(ledshim.NUM_PIXELS):
    ledshim.clear()
    ledshim.set_pixel(x,*fall)
    ledshim.show()
    time.sleep(0.2)
  reset()

def riseWalk():
  for x in range(ledshim.NUM_PIXELS):
    ledshim.clear()
    ledshim.set_pixel(x,*rise)
    ledshim.show()
    time.sleep(0.2)
  reset()

def sameWalk():
  for x in range(ledshim.NUM_PIXELS):
    ledshim.clear()
    ledshim.set_pixel(x,*same)
    ledshim.show()
    time.sleep(0.2)
  reset()


'''
CONSTANTS
ledshim.NUM_PIXELS # Returns 28
ledshim.DISPLAY_WIDTH # Resturns 28... Same as NUM_PIXELS?

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
