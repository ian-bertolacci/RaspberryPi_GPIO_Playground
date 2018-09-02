#!/usr/bin/env python3

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def init():
  GPIO.setwarnings(True) # Ignore warning for now
  GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
  GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

def pinOn( pin ):
  GPIO.output( pin, GPIO.HIGH )

def pinOff( pin ):
  GPIO.output( pin, GPIO.LOW )

def readPin( pin ):
  GPIO.input( pin )

def togglePin( pin ):
  pin_value = GPIO.input( pin )
  if pin_value == GPIO.HIGH:
    GPIO.output( pin, GPIO.LOW )
  elif pin_value == GPIO.LOW:
    GPIO.output( pin, GPIO.HIGH )
  else:
    raise RuntimeException( "pin {} was neither HIGH, nor LOW: {}".format( pin, pin_value ) )

def main():
  init()
  while True:
    togglePin( 8 )
    sleep(1)

if __name__ == "__main__":
  main()
