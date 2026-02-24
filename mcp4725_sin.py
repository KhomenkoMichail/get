import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:

    amplitude = float(input("Введите значение амплитуды: "))

    signal_frequency = float(input("Введите значение частоты сигнала: "))

    sampling_frequency = float(input("Введите значение частоты дискретизации: "))

    dac = mcp.MCP4725(5.0, verbose = False)

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
