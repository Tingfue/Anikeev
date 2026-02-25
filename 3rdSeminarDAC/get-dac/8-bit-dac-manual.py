import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(pins, GPIO.OUT)
dynamic_range = 3.3

def voltage_to_number(voltage, dynamic_range) -> int:
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(n, pins):
    out = [int(x) for x in bin(n)[2:].zfill(len(pins))]
    for i in range(len(pins)):
        GPIO.output(pins[i], out[i])
    return 0

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            if voltage == 0.0:
                break
            number = voltage_to_number(voltage, dynamic_range)
            number_to_dac(number, pins)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()


