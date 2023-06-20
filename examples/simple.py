import board
import time
from opt3001 import OPT3001

"""
     GND  3V3  SDA  SCL
ADDR 0x44 0x45 0x46 0x47
"""

i2c = board.I2C()

"""
OPT3001(i2c_bus, address)
default address is 0x44
"""
opt = OPT3001(i2c)

while True:
    print(opt.lux)
    time.sleep(0.1)
