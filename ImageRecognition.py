import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

def imrec(DZ_lat,DZ_long)

R = 6371000                                             #Radius of the Earth

DZ_lat = math.radians(DZ_lat)
DZ_long = math.radians(DZ_long)

lat1 = math.radians(cs.lat)
long1 = math.radians(cs.long)

a = math.sin((DZ_latr-lat1)/2) * math.sin((DZ_latr-lat1)/2) + math.cos(lat1) * math.cos(DZ_latr) * math.sin((DZ_longr-long1)/2) * math.sin((DZ_longr-long1)/2)t
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = R * c

x = d * math.sin(DZ_longr-long1) * math.cos(DZ_latr)
y = d * math.cos(lat1) * math.sin(DZ_latr) - math.sin(lat1)*math.cos(DZ_latr)*math.cos(DZ_longr-long1)

return x,y
