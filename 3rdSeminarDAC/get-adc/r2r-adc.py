import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def init(self, dynamic_range=3.183, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def num_to_dac(self, n):
        pins = self.bits_gpio
        # dec2bin
        out = [int(x) for x in bin(n)[2:].zfill(len(pins))]
        for i in range(len(pins)):
            GPIO.output(pins[i], out[i])
        return out

    def set_voltage(self, voltage) -> int:
        dynamic_range = self.dynamic_range
        if not (0 <= voltage <= 256):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            return 0
        return self.num_to_dac(voltage)

    def sequential_counting_adc(self):
        levels = 2**8
        for i in range(levels):
            flag = self.set_voltage(i)
            voltage = i / levels * self.dynamic_range
            compval = GPIO.input(self.comp_gpio)
            print(flag)
            time.sleep(self.compare_time)
            if compval == 1:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(i, flag, voltage))
                break
        print(voltage)
            


if __name__ == "__main__":
    try:
        adc = R2R_ADC()

        while True:
            adc.sequential_counting_adc()

    finally:
        adc.deinit()