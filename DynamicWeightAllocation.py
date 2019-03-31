# This class will contain the decision algorithm that attributes 'credibility' weights to odometry and wifi-distance
import math



def checkOutliers(odoVal, wifiVal, thresholdPerc):
    outliers = 0
    if (abs(1-(wifiVal/(odoVal))) > thresholdPerc):
        outliers = 1
    else:
        outliers = 0
    return outliers

def getPosition(odoVal, wifiVal, outliers):
    if(outliers == 1):
        newposition = odoVal
    else:
        newposition = .5*(odoVal) + .5*wifiVal

    return newposition 