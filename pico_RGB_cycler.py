#!/usr/bin/env python3
# this is micropython, not regular python

from machine import Pin, PWM
import _thread
from utime import sleep_ms
from ucollections import OrderedDict

# Setting up the Hardware
button = Pin(2, Pin.IN, Pin.PULL_DOWN)
green = PWM(Pin(3, Pin.OUT))
red = PWM(Pin(4, Pin.OUT))
blue  = PWM(Pin(5, Pin.OUT))
onboard_led = Pin(25, Pin.OUT)

# Setting up a variable to check to see if the button has been pressed and released.
global button_pressed
button_pressed = True

# Setting a default color pattern
active_color = 0

global colors
colors = OrderedDict(
    [
        ("off",			 [0, 0 ,0])
        ("white",        [128, 128, 128]),
        ("fast_rainbow", ['x', 'x', 'x']),
        ("slow_rainbow", ['y', 'y', 'y']),
        ("green",        [255, 0, 0]),
        ("red",          [0, 255, 0]),
        ("blue",         [0, 0, 255]),
    ]
)

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
    # global button_pressed
    # button_pressed = False
     
    # print("green -"+str(color_list[0]))
    green.duty_u16(color_list[0] * 256)

    # print("red -"+str(color_list[1]))
    red.duty_u16(color_list[1] * 256)
    
    # print("blue -"+str(color_list[2]))    
    blue.duty_u16(color_list[2]* 256)

    
def rainbow(delay):
    global button_pressed
    while button_pressed == False:
        for index in range(255 * 3):
            if button_pressed == True:
                break
            set_color(rgb_wave(index))
            sleep_ms(delay)

def reset_led():
    print("resetting color")
    set_color([0, 0, 0])

def button_press_handler(pinfo):
    global button_pressed
    global active_color
    button_pressed = True
    active_color += 1
    if active_color == len(colors):
        active_color = 0

# Setting up an interrupt request for the button pressanation
button.irq(trigger=Pin.IRQ_RISING, handler=button_press_handler)

def show_the_right_color(color_list):
    if color_list == ['x', 'x', 'x']:
        rainbow(10)
    elif color_list == ['y', 'y', 'y']:
        rainbow(40)
    else:
        set_color(color_list)


color_list = list(colors.keys())
print(color_list)
while True:
    #  set_color(list(colors.values())[active_color])
    if button_pressed == True:
        button_pressed = False
        reset_led()
        print("showing "+color_list[active_color])
        show_the_right_color((colors[color_list[active_color]]))
        print("button was pressed")
  
# def main():

# main()