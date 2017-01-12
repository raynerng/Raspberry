import RPi.GPIO as GPIO
import time
#blinking function
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.5)
	return
#to use raspberry pi board pin numbers
GPIO.setmode(GPIO.BOARD)
#set the output channel
GPIO.setup(37,GPIO.OUT)
#blink GPIO26 50 times
for i in range (0,5):
	blink(37)
GPIO.cleanup()
