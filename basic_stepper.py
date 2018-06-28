# Basic Stepper Code based on iStep2.py code
#Load from CLI: python3 -i basic_stepper.py
#To calibrate motors: calibrate(amount,motor)
#To autocalibrate: autocalibrate()
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

print('Use: steps4(num) or steps8(num)')

def step8(pos):
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
    GPIO.output(18,1)
    GPIO.output(23,1)
    GPIO.output(24,0)
    GPIO.output(25,0)
  elif pos==3:
    #print('Pos: 3')
    GPIO.output(18,0)
    GPIO.output(23,1)
    GPIO.output(24,0)
    GPIO.output(25,0)
  elif pos==4:
    #print('Pos: 4')
    GPIO.output(18,0)
    GPIO.output(23,1)
    GPIO.output(24,1)
    GPIO.output(25,0)
  elif pos==5:
    #print('Pos: 5')
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,1)
    GPIO.output(25,0)
  elif pos==6:
    #print('Pos: 6')
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,1)
    GPIO.output(25,1)
  elif pos==7:
    #print('Pos: 7')
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,1)
  elif pos==8:
    #print('Pos: 8')
    GPIO.output(18,1)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,1)

def step4(pos):
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

def steps8(num): # USE FOR 8 STEP COUNTER-CLOCKWISE MOTOR ROTATION
  global pos # current position
  global count # current counter
  if num > 0:
    for i in range (0, abs(num)):
      step8(pos)
      time.sleep(wait)
      count += 1 #add 1 to counter
      #--- Begin code that determines direction of rotation
      if(pos == 1):
        pos = 9
      pos -= 1 #subtract 1 from motor pos
      #--- End code that determines direction of rotation
  else:
    for i in range (0, abs(num)):
      step8(pos)
      time.sleep(wait)
      count -= 1 #subtract 1 from counter
      #--- Begin code that determines direction of rotation
      pos += 1 # add 1 to motor pos
      if(pos >= 9):
        pos = 1
      #--- End code that determines direction of rotation
  step8(0) # Turn motor off

def steps4(num): # USE FOR 4 STEP COUNTER-CLOCKWISE MOTOR ROTATION
  global pos # current position
  global count # current counter
  if num > 0:
    for i in range (0, abs(num)):
      step4(pos)
      time.sleep(wait)
      count += 1 #add 1 to counter
      #--- Begin code that determines direction of rotation
      if(pos == 1):
        pos = 5
      pos -= 1 #subtract 1 from motor pos
      #--- End code that determines direction of rotation
  else:
    for i in range (0, abs(num)):
      step4(pos)
      time.sleep(wait)
      count -= 1 #subtract 1 from counter
      #--- Begin code that determines direction of rotation
      pos += 1 # add 1 to motor pos
      if(pos >= 5):
        pos = 1
      #--- End code that determines direction of rotation
  step4(0) # Turn motor off

#GPIO.cleanup()

'''
def steps8(num): # USE FOR 8 STEP CLOCKWISE MOTOR ROTATION
  global pos # current position
  global count # current counter
  if num > 0:
    for i in range (0, abs(num)):
      step8(pos)
      time.sleep(wait)
      count += 1 #add 1 to counter
      
      #--- Begin code that determines direction of rotation
      pos += 1 # add 1 to motor pos
      if(pos >= 9):
        pos = 1
      #--- End code that determines direction of rotation
  else:
    for i in range (0, abs(num)):
      step8(pos)
      time.sleep(wait)
      count -= 1 #subtract 1 from counter
      #--- Begin code that determines direction of rotation
      if(pos == 1):
        pos = 9
      pos -= 1 #subtract 1 from motor pos
      #--- End code that determines direction of rotation
  step8(0) # Turn motor off
'''

'''
# CALIBRATION CODE
def calibrate(amount,motor): #calibrate each motor by hand
  st = amount
  if motor == 0:
    m0steps_8(st)
  elif motor == 1:
    m1steps_8(st)
  elif motor == 2:
    m2steps_8(st)
  elif motor == 3:
    m3steps_8(st)
  else:
    print("motor selector out of range")

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
