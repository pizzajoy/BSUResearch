import PinTest1
class Test:
    prevStep=0
    try:
        while(True):
            ##TODO:begin wheels
            step = PinTest1.stepCounter()
            if(step != prevStep): #reporting step
                print(PinTest1.step2cm(step))
                prevStep=step
            ## stop wheel        
    except KeyboardInterrupt:
         GPIO.cleanup()
 
        