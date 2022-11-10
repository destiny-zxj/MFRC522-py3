from time import sleep
import RPi.GPIO as GPIO
from .mfrc522.SimpleMFRC522 import SimpleMFRC522


reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        cid, text = reader.read()
        print("ID: %s\nText: %s" % (cid, text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
