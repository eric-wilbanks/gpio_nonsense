#!/usr/bin/env python3
# this is micropython, not regular python

from machine import Pin, PWM
import utime
import _thread
from time import sleep

# Setting up the Hardware
button = Pin(2, Pin.IN, Pin.PULL_DOWN)
green = PWM(Pin(3, Pin.OUT))
red = PWM(Pin(4, Pin.OUT))
blue  = PWM(Pin(5, Pin.OUT))
onboard_led = Pin(25, Pin.OUT)

# Setting up a variable to check to see if the button has been pressed and released.
button_pressed = False

# Setting a default color pattern
active_color = 0

colors = {
    "off": [0, 0, 0],
    "green": [255, 0, 0],
    "red": [0, 255, 0],
    "blue": [0, 0, 255],
    "white": [128, 128, 128]
}



def set_color(color_list):
    # resetting the button value
    global button_pressed = False
    green.duty_u16(color_list[0])
    red.duty_u16(color_list[1])
    blue.duty_u16(color_list[2])


def button_checker():
    global button_pressed = True
    global active_color =+ 1
    if active_color < 2
        active_color = 0

# Setting up an interrupt request for the button pressanation
button.irq(trigger=Pin.IRQ_RISING, handler=button_checker)

while True:
    

