import machine
import utime

sensor_pin = machine.Pin(36)
adc = machine.ADC(sensor_pin)

while True:
    raw_value = adc.read()
    voltage = raw_value / 4095 * 3.3  # Assuming 12-bit ADC
    temperature_c = (voltage - 0.5) * 100  # Simple conversion for the internal temperature sensor
    print("Temperature:", temperature_c, "°C")
    utime.sleep(2)