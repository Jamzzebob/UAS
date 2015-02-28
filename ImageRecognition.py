import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

def imrec(DZ_lat,DZ_long,cslat,cslng):
    
    R = 6371000                                             #Radius of the Earth
    
    DZ_latr = math.radians(DZ_lat)
    DZ_longr = math.radians(DZ_long)
    
    lat1 = math.radians(cslat)
    long1 = math.radians(cslng)
    
    a = math.sin((DZ_latr-lat1)/2) * math.sin((DZ_latr-lat1)/2) + math.cos(lat1) * math.cos(DZ_latr) * math.sin((DZ_longr-long1)/2) * math.sin((DZ_longr-long1)/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c

    print(d)
    
    x = (math.sin(DZ_longr-long1) * math.cos(DZ_latr))
    y = (math.cos(lat1) * math.sin(DZ_latr) - math.sin(lat1)*math.cos(DZ_latr)*math.cos(DZ_longr-long1))
    brng = math.atan2(x, y)
    brng = math.degrees(brng)
    brng = (brng+360)%360
    print(brng)
    x = d * math.sin(math.radians(brng))
    y = d * math.cos(math.radians(brng))
    return x,y
