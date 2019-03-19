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
    n= -2.3714
    d0 = 1 #values updated 03/04/19
    PLd0 = -18.667
    odoCounter = 0
    nextStop = 30
    #desiredAddress = ['72:3A:CB:C0:43:E4', '50:C7:BF:96:D4:AE', '70:3A:CB:C0:43:EA']
    #desiredAddress = ['30:FD:38:F0:DA:3B', '30:FD:38:F0:99:E8', '30:FD:38:F0:7F:2E'] # setup3ADB0,setup99E80,setup7F2E0
    desiredAddress = ['70:3A:CB:C0:43:E6', '70:3A:CB:D4:C2:15', 'CC:40:D0:17:FB:DA'] #CASA: Viger Studio, Viger living room, neighbor Netgear10
    wifiLocationX = [0, 10, 50]
    wifiLocationY = [0, 40, 10]  # relative to first point
    odometryOn = 1
    wifiOn = 1
##    try:
    
    if wifiOn == 1:
        done = 0
        while done == 0:
            try:
                startPosition = WifiData.WifiPosition(desiredAddress, wifiLocationX, wifiLocationY, n, PLd0, d0)
                done = 1
                print('Start Position', startPosition)
            except:
                print('A wifi is not available on Start Position:',datetime.datetime.now())
    
    MotorControl.Motor_Forward()  # This is the init to start the wheels
    while(True):

        #ODOMETRY
            
        if odometryOn == 1:
            odoStep = Odometry.stepCounter()
            odoDistance =(Odometry.step2cm(odoStep))
            if odoStep != prevOdoStep :  # reporting step
                #print("ODO_DISTANCE: ",odoDistance, odoStep)
                prevOdoStep= odoStep

         #COMBINATION
        
        if odoDistance >= nextStop:
            MotorControl.Motor_Stop()  # stop wheel
            print("ODO_DISTANCE: ",odoDistance, "STEP", odoStep)
            #CHECK WIFI
            if wifiOn == 1:
                WifiCurrentPosition = WifiData.WifiPosition(desiredAddress, wifiLocationX, wifiLocationY, n, PLd0, d0)
                wifiDistance = WifiData.getDist(startPosition, WifiCurrentPosition)
                print('WifiDistance:', wifiDistance)
                
            #COMBINED
            odoCounter += 1
            outliers = DynamicWeightAllocation.checkOutliers(odoDistance, wifiDistance, 0.1)
            print("OUTLIERS", outliers)
            finalPosition = DynamicWeightAllocation.getPosition(odoDistance, wifiDistance, outliers)
            if outliers == 1:
                odoCounter = 0
            print(odoCounter)
            print("FINAL DISTANCE", finalPosition)
            input("PRESS ENTER TO CONTINUE :D")
            MotorControl.Motor_Forward()
            nextStop+=30
                
##    except KeyboardInterrupt:
##        MotorControl.Motor_Stop()
##        GPIO.cleanup()
