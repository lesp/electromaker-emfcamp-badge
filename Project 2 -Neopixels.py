from machine import Neopix
from time import sleep
n = Neopix()
while True:
    n.display([0xff0000,0xff0000])
    sleep(0.2)
    n.display([0x00ff00,0x00ff00])
    sleep(0.2)
    n.display([0x0000ff,0x0000ff])
    sleep(0.2)
