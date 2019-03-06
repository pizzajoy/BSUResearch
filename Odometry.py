"""
right wheel is pin 23. 1 is light on, 0 is light off
left  wheel is pin 24. 1 is light on, 0 is light off
TODO:
- Make program that calcultes how many ticks (1) per second DONE
- Calculate  number of  ticks per rotation DONE
- Calculate  number of  rotations per meter DONE
- Output distrance traveled by the robot DONE
"""
import RPi.GPIO as GPIO
#import MotorControl.py

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
step = 0
prevX = GPIO.input(24)
currX = 0
def stepCounter():
    global currX, prevX, step
    currX = GPIO.input(24)
    if (currX != prevX):
        step += 1
        prevX = currX
    return step
def step2cm(step):
    print((step/72)*40 )
    return (step/72)*40 #returns total distance 
    # 48 ticks = 1 rotation = 20.2 centimeters
##def test():
##    step = stepCounter()
##        if(step != prevStep): #reporting step
##                stepCm =(step2cm(step))
##                print(stepCm, step)
##                prevStep=step
##                print(step)
##        if(stepCm >= 30):
##                    MotorControl.Motor_Stop() ## stop wheel        
##    except KeyboardInterrupt:
##        MotorControl.Motor_Stop()
##        GPIO.cleanup()
