import RPi.GPIO as GPIO
import time 
def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal



dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 256
maxVoltage = 3.3
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

try:

    while True:

        for value in range(256):
            time.sleep(0.005)
            signal = num2dac(value)
            voltage = value / levels * maxVoltage
            if (GPIO.input(comp) == 0) :
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
                break

finally:
    
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup(dac)