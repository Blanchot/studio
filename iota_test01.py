# Code based on Huggre's basic code:
# https://gist.github.com/huggre/a3044e6094867fe04096e0c64dc60f3b
# pyIOTA Api: https://github.com/iotaledger/iota.lib.py
# pip3 install pyota

import time
import datetime
from blinkt import set_pixel, set_brightness, show, clear
set_brightness(0.1)

# Imports the PyOTA library
from iota import Iota
from iota import Address

# URL to IOTA fullnode used when checking balance
iotaNode = "https://field.carriota.com:443"
# Create an IOTA object
api = Iota(iotaNode, "")
# Thalia Receive address:
address = [Address(b'RNSVVCTUYTCMZVTUAOUZUZSXKE9XZGUNAG9XNDLEKXFUDE9MSLAEQIJRFIFUCRFIZFCZNZAYFDJFQFELZMFOWWJNTD')]

# Function for checking address balance on the IOTA tangle. 
def checkbalance():

    print("Checking balance")
    gb_result = api.get_balances(address)
    balance = gb_result['balances']
    print('Balance is: ',balance)
    return (balance[0])

# Get current address balance at startup and use as baseline for measuring new funds being added.   
currentbalance = checkbalance()
lastbalance = currentbalance

# Define some variables
# lightbalance = 0
# balcheckcount = 0
# lightstatus = False

while True:
  currentbalance = checkbalance()
  if currentbalance > lastbalance:
    clear()
    set_pixel(0,255,0,0)
    show()
    time.sleep(300)
    clear()
    show()
    lastbalance = currentbalance
  time.sleep(5)


'''
# Main loop that executes every 1 second
while True:
    
    # Check for new funds and add to lightbalance when found.
    if balcheckcount == 10:
        currentbalance = checkbalance()
        if currentbalance > lastbalance:
            lightbalance = lightbalance + (currentbalance - lastbalance)
            lastbalance = currentbalance
        balcheckcount = 0

    # Manage light balance and light ON/OFF
    if lightbalance > 0:
        if lightstatus == False:
            print("light ON")
            GPIO.output(LEDPIN,GPIO.HIGH)
            lightstatus=True
        lightbalance = lightbalance -1       
    else:
        if lightstatus == True:
            print("light OFF")
            GPIO.output(LEDPIN,GPIO.LOW)
            lightstatus=False
 
    # Print remaining light balance     
    print(datetime.timedelta(seconds=lightbalance))

    # Increase balance check counter
    balcheckcount = balcheckcount +1

    # Pause for 1 sec.
    time.sleep(1)
'''
