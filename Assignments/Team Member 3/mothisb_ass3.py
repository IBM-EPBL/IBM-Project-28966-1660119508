import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button, TrafficLights, Buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
lights = TrafficLights(10, 9, 11)

while True:
    #Blinking LED....
    GPIO.output(25, GPIO.HIGH)
    sleep(1)
    GPIO.output(25, GPIO.LOW)
    sleep(1)

    #Trafic Lights....
    lights.red.on()
    sleep(10)
    lights.amber.on()
    sleep(5)
    lights.green.on()
    sleep(15)
    lights.off()