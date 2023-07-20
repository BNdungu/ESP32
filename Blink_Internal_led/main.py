import machine
import utime

led_pin = machine.Pin(2, machine.Pin.OUT)  #cretae an instance to standin for the built in led on the esp32

while True:   ##create an infinite loop to repeate the blink process
    led_pin.on()
    utime.sleep(1)
    led_pin.off()
    utime.sleep(1)
