import time
from machine import Pin, I2C
from servo import Servos

i2c = I2C(sda=Pin(21), scl=Pin(22))#moxing esp32
#i2c = I2C(sda=Pin('P26'), scl=Pin('P25'))#moxing stm32
servo = Servos(i2c, address=0x40, freq=50, min_us=500, max_us=2500, degrees=180)

while True:
    for i in range(0, 16):
        servo.position(i, 0)
    time.sleep_ms(500)
    for i in range(0, 16):
        servo.position(i, 180)
    time.sleep_ms(500)
