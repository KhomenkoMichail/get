import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, drange, comp_time = 0.01, verbose = False):
        self.comp_time = comp_time
        self.range = drange
        self.verbose = verbose

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def num_2_dac(self, number):
        GPIO.output(self.bits_gpio, [int(element) for element in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        for i in range(256):
            self.num_2_dac(i)
            time.sleep(self.comp_time)
            if GPIO.input(self.comp_gpio) or i == 255:
                return i * self.range / 255

    def get_sc_vol(self):
        res = self.sequential_counting_adc()
        print(f"Voltage is: {res}\n")
        return res

    def successive_approximation_adc(self):
        upper = 256
        lower = 0
        while lower < upper - 1:
            current = (lower + upper) // 2
            self.num_2_dac(current)
            time.sleep(self.comp_time)
            if GPIO.input(self.comp_gpio):
                upper = current
            else:
                lower = current
        return lower

    def bise(self):
        cmp = 128
        self.num_2_dac(cmp)
        time.sleep(self.comp_time)
        if GPIO.input(self.comp_gpio):
            cmp = 192
        else:
            cmp = 64

        self.num_2_dac(cmp)
        time.sleep(self.comp_time)
        if GPIO.input(self.comp_gpio):
            cmp += 32
        else:
            cmp -= 32

        self.num_2_dac(cmp)
        time.sleep(self.comp_time)
        if GPIO.input(self.comp_gpio):
            cmp += 16
        else:
            cmp -= 16

        self.num_2_dac(cmp)
        time.sleep(self.comp_time)
        if GPIO.input(self.comp_gpio):
            cmp += 8
        else:
            cmp -= 8

        self.num_2_dac(cmp)
        time.sleep(self.comp_time)
        if GPIO.input(self.comp_gpio):
            cmp += 4
        else:
            cmp -= 4

        self.num_2_dac(cmp)
        time.sleep(self.comp_time)
        if GPIO.input(self.comp_gpio):
            cmp += 2
        else:
            cmp -= 2

        self.num_2_dac(cmp)
        time.sleep(self.comp_time)
        if GPIO.input(self.comp_gpio):
            cmp += 1
        else:
            cmp -= 1

        return cmp

    def get_sar_vol(self):
        res = (self.successive_approximation_adc() / 255.0) * self.range
        print(f"Voltage is: {res}\n")
        return res

    def get_vol(self):
        res = (self.successive_approximation_adc() / 255.0) * self.range
        print(f"Voltage is: {res}\n")
        return res


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.183)

        while True:
            adc.get_vol()
    finally:
        adc.deinit()
