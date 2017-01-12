#import threading
#import time
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11,GPIO.OUT)
#class Button(threading.Thread):
#	"""A Thread that monitors a GPIO button"""
#
#	def __init__(self, channel):
#		threading.Thread.__init__(self)
#		self._pressed = False
#		self.channel = channel
#		#set up pin as input
#		GPIO.setup(self.channel,GPIO.IN)
#		#terminate this thread when main program finishes
#		self.daemon = True
#		#start thread running
#		self.start()
#	def pressed(self):
#		if self._pressed:
#			#clear the pressed flag now that we have detected it
#			self._pressed = False
#			return True
#		else:
#			return False
#	def run(self):
#		previous= None
#		while 1:
#			#read GPIO channel
#			current = GPIO.input(self.channel)
#			time.sleep(0.01) #wait 10ms
#			#detect change from 1 to 0( with a button press)
#			if current == False and previous == True:
#				self._pressed = True
#				#wait for flag to be cleared
#				while self._pressed:
#					time.sleep(0.05) #wait 50ms
#			previous = current
#def onButtonPress():
#	print("the button has been pressed")
#create a button thread for a button on pin 11
#button = Button(11)
#while True:
#	#ask for a name an say hello
#	name =raw_input("Enter a name or Q to quit")
#	if name.upper()==('Q'):
#		break
#	print("Hello", name)
#	#check if button has been pressed 
#	if button.pressed():
#		onButtonPress()
#
#GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN)

i=0
try:
	while True:
		name=raw_input("Enter a name or Q to quit")
		if name.upper()=="Q":
			break
		print ("Hello",name)
		if GPIO.input(37):
			print("Button has been pressed")
		i=i+1
		print(i)
finally:
	GPIO.cleanup()
