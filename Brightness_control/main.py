import machine
import utime

led_pin = machine.Pin(2, machine.Pin.OUT)
pwm = machine.PWM(led_pin)

while True:
    for duty_cycle in range(0, 1024, 32):  # Varying duty cycle to control LED brightness
        pwm.duty(duty_cycle)
        utime.sleep(0.1)
    for duty_cycle in range(1024, 0, -32):
        pwm.duty(duty_cycle)
        utime.sleep(0.1)
