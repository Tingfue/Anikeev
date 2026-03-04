import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    
    def set_number(self, n):
        pins = self.gpio_bits
        out = [int(x) for x in bin(n)[2:].zfill(len(pins))]
        for i in range(len(pins)):
            GPIO.output(pins[i], out[i])
        return 0


    def set_voltage(self, voltage) -> int:
        dynamic_range = self.dynamic_range
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            return 0
        return self.set_number(int(voltage / dynamic_range * 255))



if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
                if voltage == 0.0:
                    break
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()