import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(pins, GPIO.OUT)
