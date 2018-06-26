# BTC volume Stepper Test based on iStep2.py code
#Load from CLI: python3 -i iStep2.py
#To calibrate motors: calibrate(amount,motor)
#To autocalibrate: autocalibrate()
#Motor control based on code from here: 
#http://ingeniapp.com/en/stepper-motor-control-with-raspberry-pi/

import time
import sys
import RPi.GPIO as GPIO


motor_pas = 1 # not sure what this is for?
motor = 0 # motor counter

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# motor setup
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

print('Try motor_steps_8(value)')

def motor_step_8 (p):
  if p==0:
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)
  if p==1:
    GPIO.output(18,1)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)
  if p==2:
    GPIO.output(18,1)
    GPIO.output(23,1)
    GPIO.output(24,0)
    GPIO.output(25,0)
  if p==3:
    GPIO.output(18,0)
    GPIO.output(23,1)
    GPIO.output(24,0)
    GPIO.output(25,0)
  if p==4:
    GPIO.output(18,0)
    GPIO.output(23,1)
    GPIO.output(24,1)
    GPIO.output(25,0)
  if p==5:
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,1)
    GPIO.output(25,0)
  if p==6:
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,1)
    GPIO.output(25,1)
  if p==7:
    GPIO.output(18,0)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,1)
  if p==8:
    GPIO.output(18,1)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,1)


def motor_steps_8(value):
  #print(value)
  global motor_pas
  global motor # counter
  if(value>0): #reversed original code- was if(value<0):
    for i in range (0,abs(value)):
      motor_step_8(motor_pas)
      time.sleep(0.01)
      m0+=1 #add 1 to counter (reversed)
      motor_pas+=1
      if(motor_pas>=9):
        motor_pas=1;
  else:
    for i in range (0,abs(value)):
      m0step_8(motor_pas)
      time.sleep(0.01)
      m0-=1 #subtract 1 from counter (reversed)
      if(motor_pas==1):
        motor_pas=9;
      motor_pas-=1
  motor_step_8(0)


GPIO.cleanup()



'''
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
