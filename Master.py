import Odometry
import MotorControl
import time
import datetime
import WifiData
import DynamicWeightAllocation
import RPi.GPIO as GPIO
class Test:
    prevOdoStep = 0
    prevWifiDistance = 0
    time.sleep(2) 
    n = -1.4416
    d0 = 1 
    PLd0 = 1
    PLd = 1
    odoCounter = 0
    desiredAddress = ['72:3A:CB:C0:43:E4', '50:C7:BF:96:D4:AE', '70:3A:CB:C0:43:EA']
    wifiLocationX = [0, 10, 50]
    wifiLocationY = [0, 40, 10]  # relative to first point
    odometryOn = 1
    wifiOn = 0
    try:
        MotorControl.Motor_Forward()  # This is the init to start the wheels
        if wifiOn == 1:
            done = 0
            while done == 0:
                try:
                    startPosition = WifiData.WifiPosition(desiredAddress, wifiLocationX, wifiLocationY, n, PLd0, d0)
                    done = 1
                    print('Start Position', startPosition)
                except:
                    print('A wifi is not available on Start Position:',datetime.datetime.now())
        
        while(True):

             #WIFI

            if wifiOn == 1:
                try:
                    WifiCurrentPosition = WifiData.WifiPosition(desiredAddress, wifiLocationX, wifiLocationY, n, PLd0, d0, PLd)
                    print('got position:', WifiCurrentPosition)
                    wifiDistance = WifiData.getDist(startPosition, WifiCurrentPosition)
                    print('WifiDistance:', wifiDistance)
                    if wifiDistance != prevWifiDistance:  # reporting step
                        print(wifiDistance)
                        prevWifiDistance = wifiDistance

                except:
                    print('A wifi is not available ',datetime.datetime.now())
                     
             #ODOMETRY
                
            if odometryOn == 1:
                odoStep = Odometry.stepCounter()
                odoDistance =(Odometry.step2cm(odoStep))
                if odoStep != prevOdoStep :  # reporting step
                    print(odoDistance, odoStep)
                    prevOdoStep= odoStep

             #COMBINATION

            if odoDistance >= 30:
                MotorControl.Motor_Stop()  # stop wheel
                odoCounter += 1
                outliers = DynamicWeightAllocation.checkOutliers()
                finalPosition = DynamicWeightAllocation.getPosition(odoDistance, wifiDistance, outliers)
                if outliers == 1:
                    odoCounter = 0
                print(odoCounter)
                print(finalPosition)
                input("PRESS ENTER TO CONTINUE :D")
                MotorControl.Motor_Forward()

    except KeyboardInterrupt:
        MotorControl.Motor_Stop()
        GPIO.cleanup()
