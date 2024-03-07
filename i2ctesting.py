# i2ctesting.py

import board                           # Raspberry Pi Pico, Circuitpython
from busio import I2C
i2c = I2C(sda=board.GP4, scl=board.GP5)
while i2c.try_lock():                  # CP requires I2C bus locking
    pass

