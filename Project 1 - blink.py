from tilda import LED
from time import sleep

LED(LED.RED).on()
LED(LED.GREEN).off()

while True:
    LED(LED.RED).toggle()
    LED(LED.GREEN).toggle()
    sleep(0.1)
