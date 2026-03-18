import RPi.GPIO as GPIO
import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_hist
    

if __name__ == "__main__":
    try:
        adc = R2R_ADC()
        start = time.time()
        while time.time() - start < adc.duration:
            last_time = time.time()
            adc.time_values.append(last_time)
            adc.voltage_values.append(adc.sequential_counting_adc())
            adc.time_durations.append(abs(last_time - time.time()))
        print(adc.voltage_values, adc.time_values)
        print(adc.time_durations)
        plot_voltage_vs_time(adc.time_values, adc.voltage_values, max_voltage=3.183)
        plot_hist(adc.time_durations)
    except KeyboardInterrupt:
        print("\n\n\nsmn stopped me...\n\n\n")
    finally:
        del adc
