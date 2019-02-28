#python3 -m pip install wifi 
from wifi import Cell, Scheme
cells = Cell.all('wlan0')
wifiSsid = []
wifiSignal = []
wifiAddress = []
for cell in cells:
    wifiSsid.append(cell.ssid)
    wifiSignal.append(cell.signal)
    wifiAddress.append(cell.address)
    
print (wifiSsid, wifiSignal, wifiAddress)


