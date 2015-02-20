import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

def target():

from Droplocation import dloc 
x1, y1 = dloc()

from ImageRecognition import imrec
x2, y2 = imrec()

x3 = x1 + x2
y3 = y1 + y2
dist=math.sqrt((x3^2)+(y3^2))
theta = math.atan2(x3,y3)
R = 6371000

lat = cs.lat
long = cs.lng

lat1 = math.asin((math.sin(lat) * math.cos(dist/R))+(math.cos(lat)*math.sin(dist/R)*math.cos(theta)))
long1 = long +math.atan2(math.sin(theta)*math.sin(dist/R)*math.cos(lat) , math.cos(dist/R)-math.sin(lat)*math.sin(lat1))

retun lat1, long1
