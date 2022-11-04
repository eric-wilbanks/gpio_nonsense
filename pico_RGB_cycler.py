#!/usr/bin/env python3
# this is micropython, not regular python

# from machine import Pin, PWM
import utime
import _thread
from time import sleep

# Setting up the Hardware
# button = Pin(2, Pin.IN, Pin.PULL_DOWN)
# green = PWM(Pin(3, Pin.OUT))
# red = PWM(Pin(4, Pin.OUT))
# blue  = PWM(Pin(5, Pin.OUT))
# onboard_led = Pin(25, Pin.OUT)

# Setting up a variable to check to see if the button has been pressed and released.
# button_pressed = False

# Setting a default color pattern
active_color = 0

colors = {
    "white": [128, 128, 128]
    "green": [255, 0, 0],
    "red": [0, 255, 0],
    "blue": [0, 0, 255],
    "fast_rainbow": ['x', 'x', 'x']
    "slow_rainbow": ['x', 'x', 'x']
}

def rgb_wave(index):
    index = index % 765
    # Green decreasing, red increasing
    if index < 255:
        red = index      
        green = 255 - red
        blue = 0
    # blue increasing, red decreasing
    elif index < 510:
        blue = index - 255
        red = 255 - blue
        green = 0
    # green increasing, blue decreasing
    else:
        green = index - 510
        red = 0
        blue = 255 - green
    return green, red, blue


def set_color(color_list):
    # resetting the button value
    # global button_pressed = False\
    print("green -"+color_list[0])
    print("red -"+color_list[1])
    print("blue -"+color_list[2])
    #green.duty_u16(color_list[0])
    #red.duty_u16(color_list[1])
    #blue.duty_u16(color_list[2])


def show_rainbow(delay, delay):
    while True:
        for index in range(255 * 3):
            print(rgb(index))
            sl

def reset_led():
    set_color([0, 0, 0])

# def button_checker():
#     global button_pressed = True
#     global active_color =+ 1
#     if active_color < 2
#         active_color = 0

# Setting up an interrupt request for the button pressanation
# button.irq(trigger=Pin.IRQ_RISING, handler=button_checker)


for index in range(255 * 3):
    print(rgb_wave(index))
    
def main():
    print("main")

main()