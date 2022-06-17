from time import sleep
import RPi.GPIO as GPIO
from mfrc522.SimpleMFRC522 import SimpleMFRC522


reader = SimpleMFRC522()

try:
    reader.write('hello')
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
