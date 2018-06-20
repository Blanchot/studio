# Code test for Pimoroni's LED Shim

# LED Shim code test
# https://dbader.org/blog/python-reverse-list
# Weirdness with float subtraction... try 4.25 - 4.24
# See here for Decimal fix:
# https://stackoverflow.com/questions/14120340/python-error-in-basic-subtraction

import ledshim
import requests, json

#import random # for testing
from time import sleep

import logging
format_string = '%(levelname)s: %(asctime)s: %(message)s'
logging.basicConfig(level=logging.INFO, filename='difflog.log', format=format_string)

ledshim.set_clear_on_exit()
ledshim.set_brightness(0.5)

# RGB value tuples
rise_1 = (0,80,0) #green value (was 96 toning it down even further to 80)
rise_2 = (0,255,0)
fall_1 = (96,0,0) #red value
fall_2 = (255,0,0)
#same = (0,0,0) #version 1 no lights
same = (0,0,96) #version 2 with lights
nada = (0,0,0) #no lights

# Setting difference threshold and wait time
threshold = .03 #threshold for determining small or large rise or fall 
logging.info('Start with pos/neg threshold: {}'.format(threshold))
wait_secs = 180 #number of seconds to sleep between api calls
logging.info('Delay: {} seconds'.format(wait_secs))

prevPrice = 0
num_of_pixels = 28 # Can replace this with: ledshim.NUM_PIXELS

# Create the pixel list
pixel_list = []
for num in range(num_of_pixels):
  pixel_list.append(nada) #no lights
  #pixel_list.append(num)
  #pixel_list.append(random.choice(random_sample))

# API's Used
URL_1 = 'https://api.binance.com/api/v1/ticker/24hr?symbol=NEBLBTC' # NEBL price in BTC
URL_2 = 'https://api.coinbase.com/v2/prices/spot?currency=EUR' #Convert BTC to Euro




# Get current Binance price for NEBL (in BTC)
def get_NEBL_price_in_btc():
  try:
    r = requests.get(URL_1)
    nebl_in_BTC = json.loads(r.text)['lastPrice']
    
    #convert to float
    nebl_in_BTC = float(nebl_in_BTC)
    
    # NEBL price in BTC
    print('1 NEBL (BTC): ',nebl_in_BTC)
    
    # send nebl_in_BTC to Euro converter at Coinbase
    eurPrice = get_BTC_price_in_euros(nebl_in_BTC)
    
  except requests.ConnectionError:
    print("Error querying Binance API")



# Convert BTC to Euro and send to changeTester
def get_BTC_price_in_euros(nebl_in_BTC):
  try:
    r = requests.get(URL_2)
    btc_Euro_exchange = json.loads(r.text)['data']['amount']
    
    # NEBL price in EUR
    nebl_price_in_euros = nebl_in_BTC * float(btc_Euro_exchange)
    nebl_price_in_euros = round(nebl_price_in_euros,2) #round to two decimal places
    print('1 NEBL (EUR): {:0.2f}'.format(nebl_price_in_euros))
    
    # Send to changeTester rounded to 2 decimal places
    nebl_price_in_euros = round(nebl_price_in_euros,2)
    changeTester(nebl_price_in_euros)
  except requests.ConnectionError:
    print("Error querying Coinbase API")



''' 
# .02 OR MORE DIFF FOR LARGE RISE OR FALL 
def changeTester(nebl_price_in_euros):
  global prevPrice
  #print('Nebl price in euros: ', nebl_price_in_euros)
  print('Previous price: ', prevPrice)
  diff = round(nebl_price_in_euros - prevPrice, 2) #need to do this, see note above
  print('Diff since last check: ', diff) #can comment this out later
  
  if diff == 0.01: # value rises by 1 cent
    pixel_list.insert(0, rise_1)
    pixel_list.pop()
    print('Increased by: ', diff)
  elif diff >= 0.02: # value rises by more than 1 cent
    pixel_list.insert(0, rise_2)
    pixel_list.pop()
    print('Increased by: ', diff)
    logging.info('Diff: {}'.format(diff))
  elif diff == -0.01: # value falls by 1 cent
    pixel_list.insert(0, fall_1)
    pixel_list.pop()
    print('Decreased by: ', diff)
  elif diff <= -0.02: # value falls by more than 1 cent
    pixel_list.insert(0, fall_2)
    pixel_list.pop()
    print('Decreased by: ', diff)
    logging.info('Diff: {}'.format(diff))
  else: # value unchanged
    pixel_list.insert(0, same)
    pixel_list.pop()
    print('Price unchanged: ', diff)
  prevPrice = nebl_price_in_euros
  #print(pixel_list)
  print()
  return pixel_list



# .03 OR MORE DIFF FOR LARGE RISE OR FALL 
def changeTester(nebl_price_in_euros):
  global prevPrice
  #print('Nebl price in euros: ', nebl_price_in_euros)
  print('Previous price: ', prevPrice)
  diff = round(nebl_price_in_euros - prevPrice, 2) #need to do this, see note above
  print('Diff since last check: ', diff) #can comment this out later
  
  if diff > 0 and diff <= 0.02: # value rises by 1 or 2 cents
    pixel_list.insert(0, rise_1)
    pixel_list.pop()
    print('Small rise by: ', diff)
  elif diff >= 0.03: # value rises by 3 or more cents
    pixel_list.insert(0, rise_2)
    pixel_list.pop()
    print('Large rise by: ', diff)
    logging.info('Large rise by: {}'.format(diff))
  elif diff < 0 and diff >= -0.02: # value falls by 1 or 2 cents
    pixel_list.insert(0, fall_1)
    pixel_list.pop()
    print('Small fall by: ', diff)
  elif diff <= -0.03: # value falls by 3 or more cents
    pixel_list.insert(0, fall_2)
    pixel_list.pop()
    print('Large fall by: ', diff)
    logging.info('Large fall by: {}'.format(diff))
  else: # value unchanged
    pixel_list.insert(0, same)
    pixel_list.pop()
    print('Price unchanged: ', diff)
  prevPrice = nebl_price_in_euros
  #print(pixel_list)
  print()
  return pixel_list
'''

# USING THRESHOLD VARIABLE FOR DIFF ON LARGE RISE OR FALL 
def changeTester(nebl_price_in_euros):
  global prevPrice
  #print('Nebl price in euros: ', nebl_price_in_euros)
  print('Previous price: ', prevPrice)
  diff = round(nebl_price_in_euros - prevPrice, 2) #need to do this, see note above
  print('Diff since last check: ', diff) #can comment this out later
  
  if diff > 0 and diff < threshold: # value rises: > 0 and < than threshold
    pixel_list.insert(0, rise_1)
    pixel_list.pop()
    print('Small rise by: ', diff)
  elif diff >= threshold: # value LARGE RISE: > or = to threshold
    pixel_list.insert(0, rise_2)
    pixel_list.pop()
    print('Large rise by: ', diff)
    logging.info('Large rise by: {}'.format(diff))
  elif diff < 0 and diff > -threshold: # value falls: < 0 and > -(threshold)
    pixel_list.insert(0, fall_1)
    pixel_list.pop()
    print('Small fall by: ', diff)
  elif diff <= -0.03: # value LARGE FALL: < or = to threshold  
    pixel_list.insert(0, fall_2)
    pixel_list.pop()
    print('Large fall by: ', diff)
    logging.info('Large fall by: {}'.format(diff))
  else: # value unchanged
    pixel_list.insert(0, same)
    pixel_list.pop()
    print('Price unchanged: ', diff)
  prevPrice = nebl_price_in_euros
  #print(pixel_list)
  print()
  return pixel_list



while True:
  ledshim.clear()
  get_NEBL_price_in_btc()
  for num in range(num_of_pixels):
    ledshim.set_pixel(num, *pixel_list[num])
    #print(num, *pixel_list[num]) # Test code
  ledshim.show()
  sleep(wait_secs)



'''
# For testing
def testCode(bright_val):
  ledshim.set_brightness(bright_val)
  random_sample = [rise_1, rise_2, fall_1, fall_2, same]
  pixel_list = []
  for num in range(num_of_pixels): # seed list with random values
    pixel_list.append(random.choice(random_sample))
  ledshim.clear()
  for num in range(num_of_pixels):
    ledshim.set_pixel(num, *pixel_list[num])
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
