import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print("Button Pressed")
        subprocess.run(["/home/USER/prisma/scripts/ykushxs_on.sh"])
    else:
        print("Button Released")

GPIO.add_event_detect(26, GPIO.BOTH, callback=my_callback, bouncetime=200)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
