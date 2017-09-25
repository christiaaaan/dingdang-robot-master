#! /usr/bin/python
# -*- coding:utf-8 -*-
#本代码实现的是树莓派利用超声波模块测距
#使用超声波测距模块时,VCC接树莓派的5V,GND接树莓派GND。trig接树莓派38，echo接树莓派40.
#GPIO编码方式为BOARD！！！
import RPi.GPIO as GPIO
import time

def checkdist():

        #发出触发信号
        GPIO.output(38,GPIO.HIGH)
        #保持10us以上（我选择15us）
        time.sleep(0.000015)
        GPIO.output(38,GPIO.LOW)
        while not GPIO.input(40):
                pass
        #发现高电平时开时计时
        t1 = time.time()
        while GPIO.input(40):
                pass
        #高电平结束停止计时
        t2 = time.time()
        #返回距离，单位为厘米
        return (t2-t1)*34000/2
GPIO.setmode(GPIO.BOARD)
#第3号针，GPIO2
GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)
#第5号针，GPIO3
GPIO.setup(40,GPIO.IN)

time.sleep(2)
try:
        while True:
                print 'Distance: %0.2f cm' %checkdist()
                time.sleep(0.5)
except KeyboardInterrupt:
        GPIO.cleanup()