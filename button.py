#!/usr/bin/env python3

from gpiozero import Button
from signal import pause

def zero():
    print("zero!")

def one():
    print("one!")

def two():
    print("two!")

def three():
    print("three!")

def four():
    print("four!")

def five():
    print("five!")

button = Button(2)


count = 0

option = {
    0 : zero,
    1 : one,
    2 : two,
    3 : three,
    4 : four,
    5 : five
}

while True:    
    button.wait_for_press()
    print("button pressed")
    count += 1
    if count >= len(option):
        count = 0
    option[count]()
    button.wait_for_release()
    print("button releases")

pause()



