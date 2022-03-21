# Le code ne marche pas, aucune idée du pourquoi !!!

from time import sleep_us
from microbit import *
from machine import time_pulse_us


class MeasurementTimeout(Exception):
    def __init__(self, timeout):
        super().__init__("Measurement timeout, exceeded {} us".format(timeout))


class Ultrasonic(object):
    def __init__(self, trigger_pin, echo_pin, timeout_us=30000):
        # WARNING: Don't use PA4-X5 or PA5-X6 as echo pin without a 1k resistor

        # Default timeout is a bit more than the HC-SR04 max distance (400 cm):
        # 400 cm * 29 us/cm (speed of sound ~340 m/s) * 2 (round-trip)

        self.timeout = timeout_us
        self.trigger = trigger_pin
        self.echo    = echo_pin

        # Init trigger pin (out)
        self.trigger.write_digital(0)

    def distance_in_inches(self):
        return (self.distance_in_cm() * 0.3937)

    def distance_in_cm(self):
        # Send a 10us pulse
        self.trigger.write_digital(1)
        sleep_us(10)
        self.trigger.write_digital(0)

        # Wait for the pulse and calc its duration
        time_pulse = time_pulse_us(self.echo, 1, self.timeout)

        if time_pulse < 0:
            raise MeasurementTimeout(self.timeout)

        # Divide the duration of the pulse by 2 (round-trip) and then divide it
        # by 29 us/cm (speed of sound = ~340 m/s)
        return (time_pulse / 2) / 29
    
    def distance2_in_cm(self):
        # Send a 10us pulse
        self.trigger.write_digital(1)
        sleep_us(5)
        self.trigger.write_digital(0)

        # Wait for the pulse and calc its duration
        time_pulse = time_pulse_us(self.echo, 1, self.timeout)

        if time_pulse < 0:
            raise MeasurementTimeout(self.timeout)

        # Divide the duration of the pulse by 2 (round-trip) and then divide it
        # by 29 us/cm (speed of sound = ~340 m/s)
        return (time_pulse / 2) / 29

u = Ultrasonic(pin13, pin14)
for i in range(20):
    print(u.distance_in_cm())
    sleep(250)