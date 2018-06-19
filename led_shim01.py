# Code test for Pimoroni's LED Shim

import ledshim
import time

ledshim.set_clear_on_exit()

rise = (0,32,0) #too bright
fall = (128,0,0) #maybe too bright
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

def test():
  ledshim.clear()
  ledshim.set_pixel(0,*rise)
  ledshim.set_pixel(1,*rise)
  ledshim.set_pixel(2,*same)
  ledshim.set_pixel(3,*rise)
  ledshim.set_pixel(4,*rise)
  ledshim.set_pixel(5,*rise)
  ledshim.set_pixel(6,*same)
  ledshim.set_pixel(7,*same)
  ledshim.set_pixel(8,*fall)
  ledshim.set_pixel(9,*fall)
  ledshim.set_pixel(10,*fall) 
  ledshim.set_pixel(11,*rise)
  ledshim.set_pixel(12,*rise)
  ledshim.set_pixel(13,*same)
  ledshim.set_pixel(14,*rise)
  ledshim.set_pixel(15,*rise)
  ledshim.set_pixel(16,*rise)
  ledshim.set_pixel(17,*same)
  ledshim.set_pixel(18,*same)
  ledshim.set_pixel(19,*fall)
  ledshim.set_pixel(20,*fall)
  ledshim.set_pixel(21,*fall)
  ledshim.set_pixel(22,*rise)
  ledshim.set_pixel(23,*rise)
  ledshim.set_pixel(24,*same)
  ledshim.set_pixel(25,*rise)
  ledshim.set_pixel(26,*rise)
  ledshim.set_pixel(27,*rise)
  ledshim.show()


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
