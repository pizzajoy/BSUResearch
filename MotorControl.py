#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time
	
def Motor_Forward():
	print ('motor forward')
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)
def Motor_Backward():
	print ('motor_backward')
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)
def Motor_TurnLeft():
	print ('motor_turnleft')
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)
def Motor_TurnRight():
	print ('motor_turnright')
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)
def Motor_Stop():
	print ('motor_stop')
	GPIO.output(ENA,False)
	GPIO.output(ENB,False)
	GPIO.output(IN1,False)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)

#Pin type setup 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
########Motor driver port defination#################
ENA = 13	#//L298 Enable A
ENB = 20	#//L298 Enable B
IN1 = 16 #19	#//Motor port 1
IN2 = 19 #16	#//Motor port 2
IN3 = 26 #21	#//Motor port 3
IN4 = 21 #26	#//Motor port 4
########Infrared sensor port defination#################



#########Motor initialized to LOW##########
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
#########Infrared initialized to input，and internal pull up#########



