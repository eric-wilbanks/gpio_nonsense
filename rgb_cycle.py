#!/usr/bin/env python3

from gpiozero import PWMLED
from gpiozero import Button
from time import sleep
from signal import pause
import threading
from threading import Timer

green = PWMLED("12")
red   = PWMLED("13")
blue  = PWMLED("19")
button = Button(2)

def reset(timer1,timer2,timer3):
    green.off()
    red.off()
    blue.off()
    # print("cancelling timer: "+ str(timer1))
    timer1.cancel()
    # print("cancelling timer: "+ str(timer2))
    timer2.cancel()
    # print("cancelling timer: "+ str(timer3))
    timer3.cancel()

def show_red():
    green.off()
    red.on()
    blue.off()

def show_blue():
    green.off()
    red.off()
    blue.on()

def show_green():
    green.on()
    red.off()
    blue.off()

def show_purple():
    green.off()
    red.on()
    blue.on()

def show_white():
    green.on()
    red.on()
    blue.on()

def show_rainbow(time_period=3, ):
    kwargs={
        'on_time':0,
        'off_time':time_period,
        'fade_in_time':time_period,
        'fade_out_time':time_period,
        'n':None,
        'background':True
    }
    green_timer = Timer(
        time_period * 0, 
        green.blink,
        kwargs=kwargs
    )
    red_timer = Timer(
        time_period, 
        red.blink,
        kwargs=kwargs
    )
    blue_timer = Timer(
        time_period * 2, 
        blue.blink,
        kwargs=kwargs
    )
    green_timer.start()
    red_timer.start()
    blue_timer.start()
    return(green_timer, red_timer, blue_timer)


def main():
    # setting some variables up
    green_timer = Timer(0, next)
    red_timer = Timer(0, next)
    blue_timer = Timer(0, next)
 
    # we gotta start somewhere, might as well be at the end
    show_white()
    active_color = 6


    while True:

        
        # when Button gets pressed, color program gets cancelled, and the color profile incriments
        button.wait_for_press()     
        reset(green_timer, red_timer, blue_timer)
        active_color += 1
        
        # if we exceed the number of color patterns, we start back at 0
        if active_color >= 7:
            active_color = 0


        # upon button release, we start the next color pattern    
        button.wait_for_release()


        if active_color == 0:
            (green_timer, red_timer, blue_timer) = show_rainbow(1)
            print("fast rainbow")
        elif active_color == 1:
            (green_timer, red_timer, blue_timer) = show_rainbow()
            print("slow rainbow")
        elif active_color == 2:
            show_green()
            print("green")
        elif active_color == 3:
            show_blue()
            print("blue")
        elif active_color == 4:
            show_red()
            print("red")
        elif active_color == 5:
            show_purple()
            print("purple")
        elif active_color == 6:
            show_white()
            print("white")
    pause()

# Here we run main
main()
