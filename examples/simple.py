import board
import time
from opt3001 import OPT3001

i2c = board.I2C()

opt = OPT3001(i2c)

while True:
    print(opt.lux)
    time.sleep(0.1)
