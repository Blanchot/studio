# btc_01 a BTC watcher for boreas
# led_shim01.py code modified and extended
# beta 2: initial btc code
# four letter phat functions: http://docs.pimoroni.com/fourletterphat/

import ledshim
import fourletterphat
import requests, json

#import random # for testing
from time import sleep

import logging
format_string = '%(levelname)s: %(asctime)s: %(message)s'
logging.basicConfig(level=logging.INFO, filename='difflog.log', format=format_string)

ledshim.set_clear_on_exit()
ledshim.set_brightness(0.5)

# RGB value tuples for ledshim
rise_1 = (0,84,0) #green value (was 96 toning it down slightly to 84)
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
URL = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
#URL_1 = 'https://api.binance.com/api/v1/ticker/24hr?symbol=NEBLBTC' # NEBL price in BTC
#URL_2 = 'https://api.coinbase.com/v2/prices/spot?currency=EUR' #Convert BTC to Euro

# Get current price for 1 bitcoin in USD for Four Letter Display
def get_BTC_price_in_USD():
  try:
    r = requests.get(URL)
    BTC_in_USD = json.loads(r.text)['data']['amount']
    
    
    #convert to float and then round to int
    BTC_in_USD = float(BTC_in_USD)
    BTC_in_USD = round(BTC_in_USD)
    
    print('1 bitcoin): ',BTC_in_USD)
    return BTC_in_USD
    
  except requests.ConnectionError:
    print("Error querying Coinbase API")




# Prepare Rise and Fall Timeline for Ledshim
def make_rise_fall_list(BTC_in_USD):
  global prevPrice
  print('Previous price: ', prevPrice)
  diff = (BTC_in_USD - prevPrice) # ints not floats so no need to: round(value,2)
  print('Diff since last check: ', diff) # can comment this out later
  
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
  prevPrice = BTC_in_USD
  #print(pixel_list)
  print()
  return pixel_list




while True:
  fourletterphat.clear()
  ledshim.clear()
  
  BTC_in_USD = get_BTC_price_in_USD()
  fourletterphat.print_number_str(BTC_in_USD)
  pixel_list = make_rise_fall_list(BTC_in_USD)
  for num in range(num_of_pixels):
    ledshim.set_pixel(num, *pixel_list[num])
  
  fourletterphat.show()
  ledshim.show()
  sleep(wait_secs)



