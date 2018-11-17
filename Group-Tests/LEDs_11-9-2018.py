import RPi.GPIO as IO
import time
from sense_emu import SenseHat
IO.setmode(IO.BCM)
IO.setwarnings(False)
IO.setup(14, IO.OUT)
IO.setup(15, IO.OUT)
IO.setup(18, IO.OUT)
sense = SenseHat()
i = 0
while True:
    temp = sense.temp
    if temp <= 0:
        IO.output(14, IO.HIGH)
        IO.output(15, IO.LOW)
        IO.output(18, IO.LOW)
    elif temp < 30:
        IO.output(14, IO.LOW)
        IO.output(15, IO.HIGH)
        IO.output(18, IO.LOW)
    else:
        IO.output(14, IO.LOW)
        IO.output(15, IO.LOW)
        IO.output(18, IO.HIGH)
    
