import RPi.GPIO as GPIO, time, os
import time

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
p1 = GPIO.PWM(18,50)
p2 = GPIO.PWM(12,50)
p3 = GPIO.PWM(13,50)
p1.start(0)
p2.start(0)
p3.start(0)
GPIO.setwarnings(False)
 
enable_pin = 26
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24
 
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
GPIO.output(enable_pin, 1)
 
def forward(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)
  
def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

def RCtime1 (RCpin): # 1st photoresistor for solar panel
        reading = 0
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(22, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(22) == GPIO.LOW):
                reading += 1
        return reading
    
def RCtime2 (RCpin): # 2nd photoresistor for solar panel
        reading = 0
        GPIO.setup(27, GPIO.OUT)
        GPIO.output(27, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(27, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(27) == GPIO.LOW):
                reading += 1
        return reading

def RCtime3 (RCpin): # room 1 photoresistor
        reading = 0
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(16, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(16) == GPIO.LOW):
                reading += 1
        return reading

def RCtime4 (RCpin): # room 2 photoresistor
        reading = 0
        GPIO.setup(5, GPIO.OUT)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(5, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(5) == GPIO.LOW):
                reading += 1
        return reading

def RCtime5 (RCpin): # room 3 photoresistor
        reading = 0
        GPIO.setup(6, GPIO.OUT)
        GPIO.output(6, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(6, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(6) == GPIO.LOW):
                reading += 1
        return reading
 
while True:
        Avg= (RCtime1(22) + RCtime2(27))/2
        
        if Avg > 600:
                forward(int(5)/1000.0, int(0)) # when too dark stop spinning
        if Avg < 300:
                forward(int(5)/1000.0, int(0)) # when solar panel catches light
        if Avg > 300 and Avg < 600:
                forward(int(5)/1000.0, int(10)) # when solar panel is looking for light


        pr1 = sorted([0,RCtime3(16),10000])[1]
        p1.ChangeDutyCycle(pr1/100.0)
        
        pr2 = sorted([0,RCtime4(5),10000])[1]
        p2.ChangeDutyCycle(pr2/100.0)
        
        pr3 = sorted([0,RCtime5(6),10000])[1]
        p3.ChangeDutyCycle(pr3/100.0)

        # photoresistors values inverse proportionate to led power
