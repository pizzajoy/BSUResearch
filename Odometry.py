"""
right wheel is pin 23. 1 is light on, 0 is light off
left  wheel is pin 24. 1 is light on, 0 is light off
"""
import RPi.GPIO as GPIO
import MotorControl
import DynamicWeightAllocation


GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
step = 0
prevX = GPIO.input(24)
currX = 0
prevStep = 0
odoCounter = 0

def stepCounter():
    global currX, prevX, step
    currX = GPIO.input(24)
    if (currX != prevX):
        step += 1
        prevX = currX
    return step

def step2cm(step):
   # print((step/72)*40 )
    return (step/72)*40 #returns total distance 
    # 48 ticks = 1 rotation = 20.2 centimeters

def get_odometry_dist():
    step = stepCounter()
    return step2cm(step)

def test(odoCounter = 0,prevStep = 0, step = 0):
    step = stepCounter()
    stepCm = (step2cm(step))
    if (step != prevStep):  # reporting step
        print(stepCm, step)
        prevStep = step
        if (stepCm >= 30):
            MotorControl.Motor_Stop()  ## stop wheel
            odoCounter += 1
            if (DynamicWeightAllocation.checkOutliers() == 0):
                odoCounter = 0
            print(odoCounter)
        if (stepCm < 30):
            MotorControl.Motor_Forward()
        return step2cm(step)