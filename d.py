from machine import Pin, Timer
from utime import sleep_ms
import ubluetooth


led_a = Pin(15, Pin.OUT)
led_b = Pin(2, Pin.OUT)
led_c = Pin(4, Pin.OUT)
    
    
class BLE():
    def __init__(self, name):   
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(True)

        self.led = Pin(2, Pin.OUT)
        self.timer1 = Timer(0)
        self.timer2 = Timer(1)
        
        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()

    def connected(self):        
        self.timer1.deinit()
        self.timer2.deinit()

    def disconnected(self):        
        self.timer1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: self.led(1))
        sleep_ms(200)
        self.timer2.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: self.led(0))   

    def ble_irq(self, event, data):
        if event == 1:
            '''Central disconnected'''
            self.connected()
            self.led(1)
        
        elif event == 2:
            '''Central disconnected'''
            self.advertiser()
            self.disconnected()
        
        elif event == 3:
            '''New message received'''
          
            buffer = self.ble.gatts_read(self.rx)
            message = buffer.decode('UTF-8').strip()
            ble.send('Esp dice:' + str(message))
            ble.send('Esp dice:' + str("bienvenidos:"))
            print(message)
                                 
                   
            if message == 'led uno on':
                led_a.value(1)
                print("led uno encendido")
                ble.send(str('Led uno encendido'))
                
                
            if message == 'led uno off':
                led_a.value(0)
                print("led uno apagado")
                ble.send(str('Led uno apagado'))
            
            
            if message == 'led dos on':
                led_b.value(1)
                print("led dos encendido")
                ble.send(str('Led dos encendido'))
                
                
            if message == 'led dos off':
                led_b.value(0)
                print("led dos apagado")
                ble.send(str('Led dos apagado'))
                
            if message == 'led tres on':
                led_c.value(1)
                print("led tres encendido")
                ble.send(str('Led tres encendido'))
                
                
            if message == 'led  tres off':
                led_c.value(0)
                print("led tres apagado")
                ble.send(str('Led tres apagado'))
                
            if message == "all leds off":
                led_a.value(0)
                led_b.value(0)
                led_c.value(0)
                print("todos los leds apagados")
                ble.send(str('Todos los leds apagados'))
                
            if message == "all leds on":
                led_a.value(1)
                led_b.value(1)
                led_c.value(1)
                print("todos los leds encendidos")
                ble.send(str('Todos los leds encendidos'))
                
            if message == "parpadear": 
                
                while True:
                    
                    led_a.value(1)
                    led_b.value(1)
                    led_c.value(1)
                    sleep_ms(100)
                    led_a.value(0)
                    led_b.value(0)
                    led_c.value(0)
                    sleep_ms(100)
                    
            if message == "semaforo": 
                
                while True:
                    
                    led_c.value(0)
                    led_a.value(1)
                    sleep_ms(3000)
                    led_a.value(0)
                    led_b.value(1)
                    sleep_ms(1750)
                    led_b.value(0)
                    led_c.value(1)
                    sleep_ms(3000)
                    
            
    def register(self):        
        # Nordic UART Service (NUS)
        NUS_UUID = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
        RX_UUID = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
        TX_UUID = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'
            
        BLE_NUS = ubluetooth.UUID(NUS_UUID)
        BLE_RX = (ubluetooth.UUID(RX_UUID), ubluetooth.FLAG_WRITE)
        BLE_TX = (ubluetooth.UUID(TX_UUID), ubluetooth.FLAG_NOTIFY)
            
        BLE_UART = (BLE_NUS, (BLE_TX, BLE_RX,))
        SERVICES = (BLE_UART, )
        ((self.tx, self.rx,), ) = self.ble.gatts_register_services(SERVICES)

    def send(self, data):
        self.ble.gatts_notify(0, self.tx, data + '\n')

    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        self.ble.gap_advertise(100, bytearray('\x02\x01\x02') + bytearray((len(name) + 1, 0x09)) + name)
        


ble = BLE("El ESP32 mas malote")