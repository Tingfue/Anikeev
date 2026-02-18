import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)

a = bin(25)[2:].zfill(8)
print(a)

p = GPIO.PWM(0, 0.5)
p.start(100)
input('Press return to stop: ')
p.stop()
GPIO.cleanup()
