#!/home/pi/server
# coding=utf-8
#使用超声波测距模块时,VCC接树莓派的5V,GND接树莓派GND。trig接树莓派38，echo接树莓派40.
#GPIO编码方式为BOARD！！
import  RPi.GPIO as GPIO
import time

def t_stop():
    GPIO.output(11,False)
    GPIO.output(12,False)
    GPIO.output(15,False)
    GPIO.output(16,False)

def t_up():
    GPIO.output(11,True)
    GPIO.output(12,False)
    GPIO.output(15,True)
    GPIO.output(16,False)

def t_down():
    GPIO.output(11,False)
    GPIO.output(12,True)
    GPIO.output(15,False)
    GPIO.output(16,True)

def t_left():
    GPIO.output(11,False)
    GPIO.output(12,True)
    GPIO.output(15,True)
    GPIO.output(16,False)

def t_right():
    GPIO.output(11,True)
    GPIO.output(12,False)
    GPIO.output(15,False)
    GPIO.output(16,True)

def bee():
    GPIO.output(12,True)
    time.sleep(0.5)
    GPIO.output(12,False)
    GPIO.output(15,True)
    time.sleep(5)
    GPIO.output(12,True)
    GPIO.output(15,False)

def checkdist():

        #���������ź�
        GPIO.output(38,GPIO.HIGH)
        #����10us���ϣ���ѡ��15us��
        time.sleep(0.000015)
        GPIO.output(38,GPIO.LOW)
        while not GPIO.input(40):
                pass
        #���ָߵ�ƽʱ��ʱ��ʱ
        t1 = time.time()
        while GPIO.input(40):
                pass
        #�ߵ�ƽ����ֹͣ��ʱ
        t2 = time.time()
        #���ؾ��룬��λΪ����
        return (t2-t1)*34000/2


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(40,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)


##time.sleep(2)

try:
    while True:
        dis = int(checkdistance())
        print(dis)
        if dis <= 30:
            print"distance less than 0.30m and back"
            t_stop()
            time.sleep(0.1)
            t_down()
            time.sleep(0.5)
            t_left()
        elif dis > 30:
            print"forward"
            time.sleep(0.1)
            t_up()
except KeyboardInterrupt:
    GPIO.cleanup()

