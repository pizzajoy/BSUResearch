#python3 -m pip install wifi 
import math
# https://pypi.org/project/python-wifi/ another library for wifi
from wifi import Cell, Scheme # https://wifi.readthedocs.io/en/latest/
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

def signal2Distance(wifiSignal, n, PLd0, d0, PLd): #n= -1.4416, d0 = 1, PLd0 = 1
    #print(wifiSignal, n, PLd0, d0, PLd) 
    PLdPower = (10**PLd)/10
    distance =  d0*(10**(((-wifiSignal)-PLd0)/10*n)) 
    return distance

def robbyEquationX(wifiDistance, wifiLocationX, wifiLocationY):
    #Generalized equation
    #print(wifiDistance,wifiLocationX,wifiLocationY)
    x = (((wifiDistance[0])**2 - (wifiDistance[2])**2) - ((wifiLocationX[0])**2 - (wifiLocationX[2])**2) -  ((wifiLocationY[0])**2 - (wifiLocationY[2])**2)) / 2 * (wifiLocationX[2]-wifiLocationX[0])
    print('Robby Position X:',x)
    return x


##def robbyEquationY(wifiDistance, wifiLocationX, wifiLocationY):
##    y = ((robbyEquationX(wifiDistance)) + wifiDistance[0])**2 -((wifiDistance[1])**2 )
##    return y
    
def robbyPosition(wifiAddress, wifiLocationX, wifiLocationY, n, PLd0, d0, PLd):   #powers must be vector for x and y axis, PLd0 or
    wifiSignal = filter(wifiAddress)[1] # this is the distance (d_)
    wifiDistance = []
    print('Wifi Signal:',wifiSignal)
    for signal in wifiSignal:
        wifiDistance.append(signal2Distance(signal, n, PLd0, d0, PLd))
    print('Wifi Distance:',wifiDistance)
    robbyPosition= robbyEquationX(wifiDistance, wifiLocationX, wifiLocationY) #robbyEquationY(wifiDistance)]
    return robbyPosition
    
def getDist(p0,p1): # initial and current position of Robby
    d = math.sqrt((p0-p1)**2 + (p0-p1)**2) #p0[x,y] p1[x,y]
    return d


def test():
    n= -1.4416
    d0 = 1  #need these values
    PLd0 = 1 #
    PLd= 1#
    print(list())
    wifiLocationX = [0,10,50]
    wifiLocationY = [0,40,10] 
    desiredAddress = ['70:3A:CB:C0:43:E6', '70:3A:CB:D4:C2:15', 'CC:40:D0:17:FB:DA'] #CASA: Viger Studio, Viger living room, neighbor Netgear10
    startPosition =  robbyPosition(desiredAddress, wifiLocationX, wifiLocationY, n, PLd0, d0, PLd) #wifiAddress, wifiLocationX, wifiLocationY, n, PLd0, d0, PLd
    print(startPosition)

test()