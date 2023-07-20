import machine
import esp32
from time import sleep 

while True:
    tf= esp32.raw_temperature()
    temp = (tf-32.0)/1.8
    print(temp)
    sleep(1)