# Code test for Pimoroni's LED Shim

# LED Shim code test
# https://dbader.org/blog/python-reverse-list
# Weirdness with float subtraction... try 4.25 - 4.24
# See here for Decimal fix:
# https://stackoverflow.com/questions/14120340/python-error-in-basic-subtraction

import ledshim
#import random
import requests, json
from time import sleep

# RGB value tuples
rise = (0,96,0) #green value
fall = (128,0,0) #red value
same = (0,0,0) #no lights

prevPrice = 0
num_of_pixels = 28 # Can replace this with: ledshim.NUM_PIXELS

random_sample = [rise, fall, same]

# Create the pixel list
pixel_list = []
for num in range(num_of_pixels):
  pixel_list.append(same) #no lights
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




def changeTester(nebl_price_in_euros):
  global prevPrice
  print('Nebl price in euros: ', nebl_price_in_euros)
  print('Previous price: ', prevPrice)
  diff = round(nebl_price_in_euros - prevPrice, 2) #need to do this, see note above
  print('Diff since last check: ', diff) #can comment this out later
  if diff >= 0.01: # value rising
    pixel_list.insert(0, rise)
    pixel_list.pop() # remove last value/tuple from the list
    print('Increased by: ', diff)
  elif diff <= -0.01: # value falling
    pixel_list.insert(0, fall)
    pixel_list.pop() # remove last value/tuple from the list
    print('Decreased by: ', diff)
  else: # value unchanged
    pixel_list.insert(0, same)
    pixel_list.pop() # remove last value/tuple from the list
    print('Price unchanged: ', diff)
  prevPrice = nebl_price_in_euros
  print(pixel_list)


while True:
  ledshim.clear()
  for num in range(num_of_pixels):
    ledshim.set_pixel(num, *pixel_list[num]) # Code to try
    #print(num, *pixel_list[num]) # Test code
  ledshim.show()
  #sleep(60) # checks once a minute
  sleep(180) # checks every 3 minutes
  #sleep(300) # checks every 5 minutes



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
