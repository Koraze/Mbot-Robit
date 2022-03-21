# https://www.elecfreaks.com/learn-en/microbitExtensionModule/robit.html
# https://github.com/tinkertanker/pxt-robit
#(c) 2022 Adrien Aurore

from microbit import *
from machine import time_pulse_us
from time import sleep_us, ticks_us
from PCA9685 import PCA9685
import neopixel


J1 = [pin14, pin13]
J2 = [pin16, pin15]
J3 = [pin2,  pin1]
J4 = [pin4,  pin3]

class Robit():
    def __init__(self):
        self._np     = neopixel.NeoPixel(pin12, 2)
        self._buz    = pin0
        self._light  = pin10
        self._motors = PCA9685()
        print("light can't be used with display")
    
    def color(self, led:int, r:int, g:int, b:int): #led 0-1, rgb 0-255
        self._np[led] = (r, g, b)
        self._np.show()
    
    def buzzer(self, freq, rapport=0.5):
        if freq <= 0 :
            self._buz.read_digital()
            return
        period  = int(1000000/freq)
        rapport = int(0.5 * 1023)
        self._buz.write_analog(rapport)
        self._buz.set_analog_period_microseconds(period)

    def light(self):
        display.off()
        return self._light.read_analog()/1023
        
    def clean(self):
        self.color(0, 0, 0, 0)
        self.color(1, 0, 0, 0)
        self.buzzer(0)
        self._motors.reset()
        
    def servo(self, index, angle, freq=50, min_us=600, max_us=2400, max_angle=180): # index 0-7, value 0-max_angle
        if 8 > index >= 0 :
            self._motors.freq(freq)
            self._motors.servo(index+8, angle, min_us, max_us, max_angle)
            
    def dc_motor(self, index, power, freq=100): # index 1-4, power 0-4095
        if 4 >= index >= 1 :
            self._motors.freq(freq)
            self._motors.dc_motor(index-1, power)
            
    def stepper_motor(self, index, direction, freq=50): # index 1-2, direction bool
        if 2 >= index >= 1 :
            self._motors.freq(freq)
            self._motors.stepper_motor(index-1, direction)
            
    def line(self, J): # Valeur retournée : [right left]
        for i in range(2):
            J[i].set_pull(J[i].PULL_UP)
        return [J[1].read_digital(), J[0].read_digital()]

    def distance(self, J): # Valeur retournée : distance cm (-1:trop loin)
        a, b = 1, 0
        J[a].write_digital(0)
        sleep_us(50)
        J[a].write_digital(1)  # Send a 10us pulse
        sleep_us(50)
        J[a].write_digital(0)
        
        J[b].set_pull(J[b].NO_PULL)
        #time_pulse = time_pulse_us(J[b], 1, 30000) # Wait pulse and calc duration
        while J[b].read_digital() == False:
            pass
        t1 = ticks_us()
        while J[b].read_digital() == True:
            pass
        t1 = ticks_us() - t1
        
        if t1 < 0:
            return -1
        return t1 / 14.2