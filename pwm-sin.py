import pwm_dac as pd
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    amplitude = float(input("Введите значение амплитуды: "))

    signal_frequency = float(input("Введите значение частоты сигнала: "))

    sampling_frequency = float(input("Введите частоты частоты дискретизации: "))

    dac = pd.PWM_DAC(12, 500, 3.3, True)

    count = 0
    while True:
        voltage = amplitude*sg.get_sin_wave_amplitude(signal_frequency, 1/sampling_frequency*count)
        count += 1
        sg.wait_for_sampling_period(sampling_frequency)
        dac.set_voltage(voltage)
except ValueError:
    print("Ошибка ввода!")

finally:
    dac.deinit()
