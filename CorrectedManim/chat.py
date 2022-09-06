#!/usr/bin/env python

from pynput.keyboard import Key, Cotroller
import time
keyboard = Cotroller()

a = input('Enter your massages you want to send:')
b = eval('Enter loop times:')
print('Data received. Please put your mouse to chat box,')
time.sleep(2)
for i in range(3):
    print(r'START IN %dSECONDS!' % (3-i))
    time.sleep(1)
for i in range(b):
    keyboard.type(a)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
print('Message sent. Please close the window.')
