import Odometry
import MotorControl
import time
import datetime
import WifiData
import RPi.GPIO as GPIO
class Test:
    prevStep=0
    prevRobbyDistance = 0
    time.sleep(2) 
    n= -1.4416
    d0 = 1 
    PLd0 = 1
    PLd= 1
    desiredAddress = ['72:3A:CB:C0:43:E4', '50:C7:BF:96:D4:AE', '70:3A:CB:C0:43:EA']
    wifiLocationX = [0,10,50]
    wifiLocationY = [0,40,10] # relative to first point
    odometryOn = 1
    wifiOn = 0
    try:
        MotorControl.Motor_Forward()
        MotorControl.Motor_Stop()
        if wifiOn == 1:
            done=0
            while(done==0):
                try:
                    startPosition = WifiData.robbyPosition(desiredAddress, wifiLocationX, wifiLocationY, n, PLd0, d0, PLd) #wifiAddress, wifiLocationX, wifiLocationY, n, PLd0, d0, PLd
                    done=1
                    print('Start Position',startPosition)
                except:
                    print('A wifi is not available on Start Position:',datetime.datetime.now())
        
        while(True):
            #WIFI POSITIONING
            if(wifiOn==1):
                try:
                    robbyCurrentPosition = WifiData.robbyPosition(desiredAddress, wifiLocationX, wifiLocationY, n, PLd0, d0, PLd) #now is different, updates
                    print('got position:',robbyCurrentPosition)
                    robbyDistance = WifiData.getDist(startPosition, robbyCurrentPosition)
                    print('distance:',robbyDistance)
                    if(robbyDistance != prevRobbyDistance): #reporting step
                        print(robbyDistance)
                        prevRobbyDistance=robbyDistance
                    if robbyDistance >= 30:
                        MotorControl.Motor_Stop()
                except:
                    print('A wifi is not available ',datetime.datetime.now())
                     
             #ODOMETRY
            step = Odometry.stepCounter()
            stepCm =(Odometry.step2cm(step))
            
            if(odometryOn==1):
                if(step != prevStep): #reporting step
                    print(stepCm, step)
                    prevStep=step
                if(stepCm >= 1.8):
                    MotorControl.Motor_Stop() ## stop wheel
                if(stepCm < 1.8):
                    MotorControl.Motor_Forward()
    except KeyboardInterrupt:
        MotorControl.Motor_Stop()
        GPIO.cleanup()
 
        