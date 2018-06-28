# flag-btc01 (just the stepper code!)
#based on 4 step 'Basic Stepper Code'
#Load from CLI: python3 -i flag_btc.py
#To do: see if I can make use of older autocalibrate code...
#Motor control based on code from here: 
#http://ingeniapp.com/en/stepper-motor-control-with-raspberry-pi/

import time
import sys
import RPi.GPIO as GPIO

wait = .01 # time to pause between motor steps
pos = 1 # values 0 to 8
count = 0 # motor counter

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(True)
GPIO.setwarnings(False)

# pins setup
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

print('Use: steps(num)')



def step(pos):
  if pos==0:
    #print('Pos: 0')
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)
  elif pos==1:
    #print('Pos: 1')
    GPIO.output(18,1)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)
  elif pos==2:
    #print('Pos: 2')
    GPIO.output(18,0)
    GPIO.output(23,1)
    GPIO.output(24,0)
    GPIO.output(25,0)
  elif pos==3:
    #print('Pos: 3')
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,1)
    GPIO.output(25,0)
  elif pos==4:
    #print('Pos: 4')
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,1)



def steps(num): # 4 STEP COUNTER-CLOCKWISE MOTOR ROTATION
  global pos # current position
  global count # current counter
  if num > 0:
    for i in range (0, abs(num)):
      step(pos)
      time.sleep(wait)
      count += 1 #add 1 to counter
      #--- Begin code that determines direction of rotation
      if(pos == 1):
        pos = 5
      pos -= 1 #subtract 1 from motor pos
      #--- End code that determines direction of rotation
  else:
    for i in range (0, abs(num)):
      step(pos)
      time.sleep(wait)
      count -= 1 #subtract 1 from counter
      #--- Begin code that determines direction of rotation
      pos += 1 # add 1 to motor pos
      if(pos >= 5):
        pos = 1
      #--- End code that determines direction of rotation
  step(0) # Turn motor off


#GPIO.cleanup()


'''
# CALIBRATION CODE

def autocalibrate(): #reverse 'last positions' for autocalibration
  global m0
  global m1
  global m2
  global m3
  f_in = open('last_positions', 'rt') 
  read_str = f_in.read()
  f_in.close()
  
  read_pos_list = read_str.split()
  print(read_pos_list)
  # turn each element of the list into an int and reverse its sign
  recalib_m0 = (int(read_pos_list[0])) * -1
  recalib_m1 = (int(read_pos_list[1])) * -1
  recalib_m2 = (int(read_pos_list[2])) * -1
  recalib_m3 = (int(read_pos_list[3])) * -1
  m0steps_8(recalib_m0)
  m1steps_8(recalib_m1)
  m2steps_8(recalib_m2)
  m3steps_8(recalib_m3)
  
  #Reset each motor to 0
  m0 = 0
  m1 = 0
  m2 = 0
  m3 = 0

#GPIO.cleanup()
'''
