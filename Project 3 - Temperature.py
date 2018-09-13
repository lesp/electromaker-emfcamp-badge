from tilda import Sensors
from time import sleep

while True:
    temperature = Sensors.get_tmp_temperature()
    print(temperature)
    sleep(1)
    
