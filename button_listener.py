#!/bin/python

import RPi.GPIO as GPIO
import time
from stopwatch import StopWatch
from simpleWriter import SimpleWriter
from buttonProcessor import ButtonProcessor



writer = SimpleWriter()
processor = ButtonProcessor()

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(processor.btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(processor.btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(processor.btn3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(processor.btn4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(processor.btn5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(processor.btn6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(processor.btn7, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.add_event_detect(
    processor.btn1, GPIO.RISING, callback=processor.button1Pressed, bouncetime=250)
GPIO.add_event_detect(
    processor.btn2, GPIO.RISING, callback=processor.buttonPressed, bouncetime=250)
GPIO.add_event_detect(
    processor.btn3, GPIO.RISING, callback=processor.buttonPressed, bouncetime=250)
GPIO.add_event_detect(
    processor.btn4, GPIO.RISING, callback=processor.buttonPressed, bouncetime=250)
GPIO.add_event_detect(
    processor.btn5, GPIO.RISING, callback=processor.buttonPressed, bouncetime=250)
GPIO.add_event_detect(
    processor.btn6, GPIO.RISING, callback=processor.buttonPressed, bouncetime=250)
GPIO.add_event_detect(
    processor.btn7, GPIO.RISING, callback=processor.buttonPressed, bouncetime=250)

while True:
    if processor.state is not None:
        writer.writeState(processor.state)
    time.sleep(1)




# while True:
#     GPIO.wait_for_edge(btn1, GPIO.RISING)
#     buttonPressed(btn1)
#     time.sleep(.25)
