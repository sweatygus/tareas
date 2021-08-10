from machine import Pin, ADC
import utime

blu = Pin (15, Pin.OUT)
grn = Pin(2, Pin.OUT)
red = Pin(4, Pin.OUT)
sensor = ADC(Pin(36))

while True:
    
    lecture = float (sensor.read_u16())
    print(lecture)
    utime.sleep(0.3)
    
    if lecture > 20000:
        
        blu.value(0)
        grn.value(0)
        red.value(0)
        
    elif lecture < 19000 and lecture > 17000:
        
        blu.value(0)
        grn.value(0)
        red.value(1)
        
    elif lecture < 16900 and lecture > 14000:
    
        blu.value(0)
        grn.value(1)
        red.value(0)
        
    elif lecture < 13900 and lecture > 11000:
    
        blu.value(1)
        grn.value(0)
        red.value(0)
        
    elif lecture < 10900 and lecture > 7000:
    
        blu.value(0)
        grn.value(1)
        red.value(1)
        
    elif lecture < 6900 and lecture > 3000:
    
        blu.value(1)
        grn.value(1)
        red.value(0)
        
    elif lecture < 2900 and lecture > 1000:
        
        blu.value(1)
        grn.value(0)
        red.value(1)
    
    elif lecture < 900:
    
        blu.value(1)
        grn.value(1)
        red.value(1)