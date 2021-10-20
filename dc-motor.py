import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

pwm=GPIO.PWM(22,100) 

pwm.start(100)
x =100

while x > -1:
  pwm.ChangeDutyCycle(x)
  sleep(0.02) 

pwm.stop() 
GPIO.cleanup()