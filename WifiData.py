#python3 -m pip install wifi
import math
from wifi import Cell, Scheme # https://wifi.readthedocs.io/en/latest/
import time
# https://pypi.org/project/python-wifi/ another library for wifi
def list():
    cells = Cell.all('wlan0')
    wifiSsid = []
    wifiSignal = []
    wifiAddress = []
    for cell in cells:
        wifiSsid.append(cell.ssid)
        wifiSignal.append(cell.signal)
        wifiAddress.append(cell.address)
    list = [wifiSsid, wifiSignal, wifiAddress]
    return list


def filter(wifiAddressIn):

    l = list()
    wifiSsid = []
    wifiSignal = []
    wifiAddress = []
    for address in wifiAddressIn:
        try:
            searchIndex = l[2].index(address)
            wifiSsid.append(l[0][searchIndex])
            wifiSignal.append(l[1][searchIndex])
            wifiAddress.append(l[2][searchIndex])
        except:
            print('Address not found: ', address)
    return [wifiSsid, wifiSignal, wifiAddress]

def signal2Distance(wifiSignal, n, PLd0, d0): 
    #print(wifiSignal, n, PLd0, d0, PLd) 
    distance =  d0*10**((wifiSignal-PLd0)/(10*n))
    distanceCm = distance/0.032808
    return distanceCm

def robbyEquationX(wifiDistance, wifiLocationX, wifiLocationY):
    #Generalized equation
    print(wifiDistance,wifiLocationX,wifiLocationY)
    #x = (((wifiDistance[0])**2 - (wifiDistance[2])**2)- ((wifiLocationX[0])**2 - (wifiLocationX[2])**2) -  ((wifiLocationY[0])**2 - (wifiLocationY[2])**2)) / 2 / (wifiLocationX[2]-wifiLocationX[0])
    x = wifiDistance[0]
    #print('Robby Position X:',x)
    print('D1, D3:', wifiDistance[0], wifiDistance[2])
    
    return x


##def robbyEquationY(wifiDistance, wifiLocationX, wifiLocationY):
##    y = ((robbyEquationX(wifiDistance)) + wifiDistance[0])**2 -((wifiDistance[1])**2 )
##    return y
    
def WifiPosition(wifiAddress, wifiLocationX, wifiLocationY, n, PLd0, d0):   #powers must be vector for x and y axis, PLd0 or
    wifiSignal = filter(wifiAddress)[1] # this is the distance (d_)
    wifiDistance = []
    print('Wifi Signal:',wifiSignal)
    for signal in wifiSignal:
        wifiDistance.append(signal2Distance(signal, n, PLd0, d0))
    #print('Wifi Distance:',wifiDistance)
    robbyPosition= robbyEquationX(wifiDistance, wifiLocationX, wifiLocationY) #robbyEquationY(wifiDistance)]
    #print('Robby Position:',robbyPosition)
    return robbyPosition
    
def getDist(p0,p1): # initial and current position of Robby
    d = math.sqrt((p0-p1)**2 + (p0-p1)**2) #p0[x,y] p1[x,y]
    return d


def test():
    n= -2.3714
    d0 = 1 #values updated 03/04/19
    PLd0 = -18.667
    #PLd= 10
    print(signal2Distance(-43, -2.3714, -18.667, 1))
    print(list())
    wifiLocationX = [0,60.96, 60.96] #needs to be in centimeters
    wifiLocationY = [0,60.96,60.96] 
    desiredAddress = ['30:FD:38:F0:DA:3B', '30:FD:38:F0:99:E8', '30:FD:38:F0:7F:2E'] # setup3ADB0,setup99E80,setup7F2E0
    #desiredAddress = ['70:3A:CB:C0:43:E6', '70:3A:CB:D4:C2:15', 'CC:40:D0:17:FB:DA'] #CASA: Viger Studio, Viger living room, neighbor Netgear10
    for i in range(6):
        start = time.time()
        startPosition =  WifiPosition(desiredAddress, wifiLocationX, wifiLocationY, n, PLd0, d0) #wifiAddress, wifiLocationX, wifiLocationY, n, PLd0, d0
        print("I:",i," Time: ", time.time()-start)

#test()

        
