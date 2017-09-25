#!/usr/bin/python  
# coding=utf-8  
#本段代码实现树莓派智能小车的红外避障效果
#代码使用的树莓派GPIO是用的BOARD编码方式。 
import RPi.GPIO as GPIO  
import time  
import sys  
def t_stop():
	GPIO.output(11, False)
	GPIO.output(12, False)
	GPIO.output(15, False)
	GPIO.output(16, False)

def t_up():
	GPIO.output(11, True)
	GPIO.output(12, False)
	GPIO.output(15, True)
	GPIO.output(16, False)

def t_down():
	GPIO.output(11, False)
	GPIO.output(12, True)
	GPIO.output(15, False)
	GPIO.output(16, True)

def t_left():
	GPIO.output(11, False)
	GPIO.output(12, True)
	GPIO.output(15, True)
	GPIO.output(16, False)

def t_right():
	GPIO.output(11, True)
	GPIO.output(12, False)
	GPIO.output(15, False)
	GPIO.output(16, True)

def bee():
	GPIO.output(12, True)
	time.sleep(0.5)
	GPIO.output(12, False) 
	GPIO.output(15, True)
	time.sleep(5) 
	GPIO.output(12, True) 
	GPIO.output(15, False)


GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(37,GPIO.IN)
GPIO.setup(38,GPIO.IN)
def det():
	while True:
		if GPIO.input(37)==False and GPIO.input(38)==False:
		#当左右两侧检测的信号均为低时（遇到障碍物），小车倒退0.5S后左转直至信号产生变化
			print "back"
			time.sleep(0.1)
			t_down()
			time.sleep(0.5)
			t_left()
		elif  GPIO.input(37)==True and GPIO.input(38)==False:
		#当右侧检测的信号均为低时（右侧遇到障碍物），小车左转直至信号产生变化
			print "Left"
			time.sleep(0.1)
			t_left()
		elif  GPIO.input(37)==False and GPIO.input(38)==True:
		#当左侧检测的信号均为低时（左侧遇到障碍物），小车左转直至信号产生变化
			print "Right"
			time.sleep(0.1)
			t_right()
		elif GPIO.input(37)==True and GPIO.input(38)==True:
		#当左右两侧检测的信号均为高时（前方无障碍物），小车前进直至信号产生变化
			print "go"
			time.sleep(0.1)
			t_up()
			
		
		
det()