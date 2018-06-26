# BTC Market Volume Test
# b1 first test
# API documentation: https://min-api.cryptocompare.com 

import datetime
import requests, json
from time import sleep

'''
import logging
format_string = '%(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, filename='BTC_volume_log.log', format=format_string)
logging.info('Start BTC Volume Log')
'''

interval_List = (2,7,12,17,22,27,32,37,42,47,52,57) #times to check- 2 min after each 5 min interval

# Hour API
URL1 = "https://min-api.cryptocompare.com/data/exchange/histohour?tsym=USD&limit=1"
# Minute API
URL2 = "https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=2"
# 5 Minute API
URL3 = "https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&aggregate=5&limit=3"

# get BTC market volume using the Cryptocompare HOUR API
def get_BTC_hour_volume():
  try:
    r = requests.get(URL1)
    market_volume_txt = json.loads(r.text)
    time1 = json.loads(r.text)['Data'][0]['time']
    volume1 = json.loads(r.text)['Data'][0]['volume']
    time2 = json.loads(r.text)['Data'][1]['time']
    volume2 = json.loads(r.text)['Data'][1]['volume']
    
    print(market_volume_txt)
    print()
    print('Time 1: ', time1)
    print(convert_seconds(time1))
    print('Volume 1: ', volume1)
    print('Volume 1: ', '{:,}'.format(volume1))
    print()
    print('Time 2: ', time2)
    print(convert_seconds(time2))
    print('Volume 2: ', volume2)
    print('Volume 2: ', '{:,}'.format(volume2))
    print()
    print('Vol2 - Vol1: ', volume2 - volume1)
    print('Vol2 - Vol1: ', '{:,}'.format(volume2 - volume1))
  except requests.ConnectionError:
    print("Error querying Cryptocompare API")



# get BTC market volume using the Cryptocompare MINUTE API
def get_BTC_min_volume():
  try:
    r = requests.get(URL2)
    market_volume_txt = json.loads(r.text)
    time1 = json.loads(r.text)['Data'][0]['time']
    volume1 = json.loads(r.text)['Data'][0]['volumefrom']
    time2 = json.loads(r.text)['Data'][1]['time']
    volume2 = json.loads(r.text)['Data'][1]['volumefrom']
    time3 = json.loads(r.text)['Data'][2]['time']
    volume3 = json.loads(r.text)['Data'][2]['volumefrom']
    
    print(market_volume_txt)
    print()
    print('Time 1: ', time1)
    print(convert_seconds(time1))
    print('Volume 1: ', volume1)
    #print('Volume 1: ', '{:,}'.format(volume1))
    print()
    print('Time 2: ', time2)
    print(convert_seconds(time2))
    print('Volume 2: ', volume2)
    #print('Volume 2: ', '{:,}'.format(volume2))
    print()
    print('Time 3: ', time3)
    print(convert_seconds(time3))
    print('Volume 3: ', volume3)
    #print('Volume 2: ', '{:,}'.format(volume2))
    '''
    print('Vol2 - Vol1: ', volume2 - volume1)
    print('Vol2 - Vol1: ', '{:,}'.format(volume2 - volume1))
    '''
  except requests.ConnectionError:
    print("Error querying Cryptocompare API")



# get BTC market volume using the Cryptocompare 5 MINUTE API
def get_BTC_5_min_volume():
  try:
    r = requests.get(URL3)
    market_volume_txt = json.loads(r.text)
    #time1 = json.loads(r.text)['Data'][0]['time']
    #volume1 = json.loads(r.text)['Data'][0]['volumefrom']
    #time2 = json.loads(r.text)['Data'][1]['time']
    #volume2 = json.loads(r.text)['Data'][1]['volumefrom']
    time3 = json.loads(r.text)['Data'][2]['time']
    volume3 = json.loads(r.text)['Data'][2]['volumefrom']
    #time4 = json.loads(r.text)['Data'][3]['time']
    #volume4 = json.loads(r.text)['Data'][3]['volumefrom']
    
    '''
    print(market_volume_txt)
    print()
    print('Time 1: ', time1)
    print(convert_seconds(time1))
    print('Volume 1: ', volume1)
    #print('Volume 1: ', '{:,}'.format(volume1))
    print()
    print('Time 2: ', time2)
    print(convert_seconds(time2))
    print('Volume 2: ', volume2)
    #print('Volume 2: ', '{:,}'.format(volume2))
    print()
    print('Time 3: ', time3)
    print(convert_seconds(time3))
    print('Volume 3: ', volume3)
    return time3, volume3
    #print('Volume 3: ', '{:,}'.format(volume2))
    print()
    print('Time 4: ', time4)
    print(convert_seconds(time4))
    print('Volume 4: ', volume4)
    #print('Volume 4: ', '{:,}'.format(volume2))
    '''
  except requests.ConnectionError:
    print("Error querying Cryptocompare API")



    
def convert_seconds(secs):
  converted = datetime.datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
  return converted



while True:
  tijd = time.localtime() #create a struct_time object
  if tijd[4] in interval_List: #and check if the number of minutes is in the interval_List
    time3, volume3 = get_BTC_5_min_volume()
    print()
    vol_time = convert_seconds(time3)
    print(vol_time)
    print('5 minute volume: ', volume3)
    logging.info('{}: {}'.format(vol_time, volume3))


'''
#get_BTC_hour_volume()
#get_BTC_min_volume()
get_BTC_5_min_volume()
'''
