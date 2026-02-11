import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

photo_pin = 6

GPIO.setup (photo_pin, GPIO.IN)

while True:
    photo_state = GPIO.input(photo_pin)
    GPIO.output(led, not photo_state)