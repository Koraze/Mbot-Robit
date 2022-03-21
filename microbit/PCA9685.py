# https://www.elecfreaks.com/learn-en/microbitExtensionModule/robit.html
# https://www-users.cs.york.ac.uk/~pcc/Circuits/dome/datasheet/PCA9685_2.pdf
# https://github.com/adafruit/micropython-adafruit-pca9685
# https://github.com/tinkertanker/pxt-robit
#(c) 2022 Adrien Aurore

from microbit import *
from machine import time_pulse_us
from time import sleep_us, ticks_us
import struct


def crop(value, min_, max_):
    if value < min_ :
        return int(min_)
    if value > max_ :
        return int(max_)
    return int(value)

class PCA9685():
    L     = [2047, 4095, 1023, 3071]
    H     = [4095, 2047, 3071, 1023]
    front = [0, 3, 1, 2]
    back  = [2, 1, 3, 0]
    
    def __init__(self, i2c=i2c, address=0x40):
        self._i2c       = i2c
        self._address   = address
        self._frequency = 0
        self._period_us = 0
        self.reset()

    def _write(self, register, value):
        buf = [register] + value if type(value) is list else [register, value]
        buf = bytearray(buf)
        i2c.write(self._address, buf)
        # self._i2c.writeto_mem(self._address, register, bytearray([value]))

    def _read(self, register, size=1):
        i2c.write(self._address, bytearray([register]))
        return i2c.read(self._address, size)
        # self._i2c.readfrom_mem(self._address, address, 1)[0]
        
    def reset(self):
        self._write(0x00, 0x00) # Mode1
        self.freq(50)
        for i in range(16):
            self.pwm(i, 0, 0)
        self.freq(50)

    def freq(self, freq=None):
        if freq is None:
            return int(25000000.0 / 4096 / (self._read(0xfe) - 0.5))
        if freq > 0 and freq != self._frequency :
            prescale = int(25000000.0 / 4096.0 / freq + 0.5)
            old_mode = self._read(0x00)[0] # Mode 1
            self._write(0x00, (old_mode & 0x7F) | 0x10) # Mode 1, sleep
            self._write(0xfe, prescale) # Prescale
            self._write(0x00, old_mode) # Mode 1
            sleep_us(5)
            self._write(0x00, old_mode | 0xa1) # Mode 1, autoincrement on
            self._frequency = freq
            self._period_us = 1000000 / freq

    def pwm(self, index, on=None, off=None): # index 0-15, on/off 0-4095
        index = crop(index, 0, 15)
        if on is None or off is None:
            data = self._read(0x06 + 4 * index, 4)
            print(data)
            return struct.unpack('<HH', data)
        on  = crop(on,  0, 4095)
        off = crop(off, 0, 4095)
        data = [on%0x100, on//0x100, off%0x100, off//0x100]
        self._write(0x06 + 4 * index,  data)

    def duty(self, index, value=None): # index 0-15, value 0-4095
        if value is None:
            return self.pwm(index)[1]
        self.pwm(index, 0, value)
        
    def servo(self, index, angle, min_us=600, max_us=2400, max_angle=180): # index 0-15, value 0-max_angle
        if 15 >= index >= 0 :
            min_duty  = int(4095 * min_us / self._period_us)
            max_duty  = int(4095 * max_us / self._period_us)
            size_duty = max_duty - min_duty
            duty      = int(min_duty + size_duty * angle / max_angle)
            self.duty(index, duty)
        
    def dc_motor(self, index, power): # index 0-8, value max +-4095
        if 8 > index >= 0 :
            if power >= 0 :
                self.duty(index*2,    power)
                self.duty(index*2+1,  0)
            else :
                self.duty(index*2,    0)
                self.duty(index*2+1, -power)
        
    def stepper_motor(self, index, direction): # index 0-4, direction boolean
        if 4 > index >= 0 :
            if direction :
                for i in range(4):
                    self.pwm(index+PCA9685.front[i], PCA9685.L[i], PCA9685.H[i])
            else :
                for i in range(4):
                    self.pwm( index+PCA9685.back[i], PCA9685.L[i], PCA9685.H[i])
