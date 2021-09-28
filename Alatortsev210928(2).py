import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits= len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

GPIO.setmode (GPIO.BCM)
GPIO.setup(dac, GPIO.OUT,  initial = GPIO.LOW)

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return


try:
    while True:
        for i in range (255, -1, -1):
            value = i
            signal = bin2dac(value)
            voltage = value / levels * maxVoltage
            print('Entered value = {:3} -> {}, output voltage = {:.2f}'.format(value, signal, voltage))
            sleep (0.00001)
        for i in range (0, 256):
            value = i
            signal = bin2dac(value)
            voltage = value / levels * maxVoltage
            print('Entered value = {:3} -> {}, output voltage = {:.2f}'.format(value, signal, voltage))
            sleep (0.02)


finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO clenup completed")
