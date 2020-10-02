#!/usr/bin/env python3
"""
@author: Jennifer Nguyen
"""

import time
import RPi.GPIO as gpio

# light switch class
class lightSwitch():
    def __init__(self, pin):
        gpio.setmode(gpio.BOARD)
        self.pin = pin
        gpio.setup(self.pin, gpio.OUT)
        self.dn = 5.5
        self.md = 7
        self.up = 9
        self.pwm = gpio.PWM(self.pin, 50)
        self.pwm.start(self.md)
    def close(self):
        self.pwm.stop()
        gpio.cleanup()

    # sleep/pause
    def __wait(self):
        time.sleep(0.5)

    # go to a position
    def __go(self, pos):
        self.pwm.ChangeDutyCycle(pos)
        self.__wait()

    # netural position
    def __home(self, shift = 0):
        self.__go(self.md + shift)

    # flip light switch on/off; added shift due to some issues with hallway
    def __flip_switch(self, pos, shift):
        self.__home(shift = shift)
        self.__go(pos)
        self.__home()
    def on(self):
        self.__flip_switch(self.up, shift = -1)
    def off(self):
        self.__flip_switch(self.dn, shift = 1)

