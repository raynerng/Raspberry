import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#set up pin 11 to output
GPIO.setup(11,GPIO.OUT)

state=False
while 1:
	GPIO.output(11,state)
	command=raw_input("press return to switch the led on/off or 'Q' to quit")
	if command.strip().upper().startswith('Q'):
		break	
	state = not state
