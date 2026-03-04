import RPi.GPIO as GPIO
import time

dac = [26, 20, 19, 16, 13, 12, 25, 11]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.183
trmod = 17
comparator = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(trmod, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)
GPIO.setwarnings(False)

def num2dac(val, dac):
    signal = [int(x) for x in bin(val)[2:].zfill(len(dac))]
    GPIO.output(dac, signal)
    return signal


def sequential_counting_adc(dac, maxVoltage, comparator):
    levels = 2**8
    for val in range(levels):
        flag = num2dac(val, dac)
        voltage = val / levels * maxVoltage
        compval = GPIO.input(comparator)
        print(flag)
        time.sleep(0.01)
        if compval == 1:
            print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(val, flag, voltage))
            break
    print(voltage)

try:
    while True:
        sequential_counting_adc(dac, maxVoltage, comparator)
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('sosi')