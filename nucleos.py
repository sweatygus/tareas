from machine import Pin
import utime
import _thread

cero = Pin(15, Pin.OUT)
uno = Pin(2, Pin.OUT)
dos = Pin(4, Pin.OUT)
tres = Pin(16, Pin.OUT)
cuatro = Pin(17, Pin.OUT)
cinco = Pin(5, Pin.OUT)
seis = Pin(18, Pin.OUT)
siete = Pin(19, Pin.OUT)
time = (0.03)

leds = [cero,uno,dos,tres,cuatro,cinco,seis,siete]

def derecha():
    
    while True:
        for i in leds[0:4:1]:
        
            i.value(1)
            utime.sleep_ms(10)
            i.value(0)
            utime.sleep_ms(10)
    
_thread.start_new_thread(derecha, ())
    
def izquierda():
    for i in leds[8:3:-1]:
        
        i.value(1)
        utime.sleep_ms(300)
        i.value(0)
        utime.sleep_ms(300)
        

while True:
      izquierda()
      utime.sleep(0.1)
        
        