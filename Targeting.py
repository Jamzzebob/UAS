#This Module Defines the Function target() which can be called to calculate the coordinates of the dropzone

import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

def target():                                         #Define the Function

from Droplocation import dloc                         #Import the Droppoint Calculator Function
x1, y1 = dloc()                                       #Find the position of the Droppoint realative to the dropzone

from ImageRecognition import imrec                    #Import the Image Recognition Function
x2, y2 = imrec()                                      #Find the position of the Dropzone realtive to the UAS

lat = cs.lat                                          #Pull the Latitude of the UAS
long = cs.lng                                         #Pull the Longitude of the UAS

x3 = x1 + x2                                          #Calculate the x position of the Droppoint Relative to the UAS
y3 = y1 + y2                                          #Calculate the y position of the Droppoint Relative to the UAS
dist=math.sqrt((x3^2)+(y3^2))                         #Calculate Distance to Droppoint from UAS
theta = math.atan2(x3,y3)                             #Calculate Angle of the Droppoint from the UAS
R = 6371000                                           #Radius of the earth

lat1 = math.asin((math.sin(lat) * math.cos(dist/R))+(math.cos(lat)*math.sin(dist/R)*math.cos(theta)))
#Calculate the Latitude of the Droppoint
long1 = long +math.atan2(math.sin(theta)*math.sin(dist/R)*math.cos(lat) , math.cos(dist/R)-math.sin(lat)*math.sin(lat1))
#Calculate the LOngitude of the Droppoint

retun lat1, long1                                     #Output the Latitude and Longitude of the Droppoint                                
