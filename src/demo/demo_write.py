import RPi.GPIO as GPIO
from src.mfrc522.SimpleMFRC522 import SimpleMFRC522


reader = SimpleMFRC522()

try:
    reader.write('hello' * 10)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
