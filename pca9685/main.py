import time
from servo import Servos
from machine import I2C, Pin

i2c = I2C(sda=Pin('P5'), scl=Pin('P4'))
servo = Servos(i2c, address=0x40, freq=50, min_us=650, max_us=2800, degrees=180)

while True:
    for i in range(0, 8):
        servo.position(i, 0)
    time.sleep(500)
    for i in range(0, 8):
        servo.position(i, 180)
    time.sleep(500)
