from machine import Pin
import utime

red = Pin(15, Pin.OUT)
yellow = Pin(2, Pin.OUT)
green = Pin(4, Pin.OUT)

while True:
    red.value(1)
    print("rojo")
    utime.sleep(1)
    red.value(0)
    yellow.value(1)
    print("amarillo")
    utime.sleep(0.5)
    yellow.value(0)
    green.value(1)
    print("verde")
    utime.sleep(1)
    yellow.value(1)
    print("amarillo")
    green.value(0)
    utime.sleep(0.5)
    yellow.value(0)
    
