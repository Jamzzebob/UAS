import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

def targetloc(DZ_lat,DZ_long):                          #Define the function

x,y = 0,0                                               #Initilise x and y

From ImageRecognition import imrec                      #Import the image recognition
while True:                                              #Loop the image recognition intil the target is identified
  x, y = imrec(DZ_lat,DZ_long)
  dist = cs.wp_dist                                       #Get distance to waypoint
  wpno = cs.wpno                                        #Get Waypoint Number
  if (x,y != 0,0):
    break
  if (dist <= 20):                                           #Break if within 20m of dropzone
    print 'dropzone not found'
    break
  if (wpno >= 4):                                       #Break if past dropzone
    print 'dropzone not found'
    break

lat = math.radians(cs.lat)                                            #Pull the currrent UAS latitude
long = math.radians(cs.lng)                                           #Pull the current UAS longitude

dist=math.sqrt((x**2)+(y**2))                             #Calcualte the distance to the dropzone
theta = (math.atan2(x,y)+(2*math.pi)) % (2*math.pi)                                 #Calculate the angle to the drop zone
R = 6371000                                             #Radius of the Earth

lat1 = ( math.asin((math.sin(lat) * math.cos(dist/R))+(math.cos(lat)*math.sin(dist/R)*math.cos(theta))))
#Calculate the latitude of the dropzone
long1 = (long +math.atan2(math.sin(theta)*math.sin(dist/R)*math.cos(lat) , math.cos(dist/R)-math.sin(lat)*math.sin(lat1)))
#Calculate the longitude of the dropzone

DZ_latr = math.radians(DZ_lat)
DZ_longr = math.radians(DZ_lat)

a = math.sin((lat1-DZ_latr)/2) * math.sin((lat1-DZ_latr)/2) + math.cos(DZ_latr) * math.cos(lat1) * math.sin((long1-DZ_longr)/2) * math.sin((long1-DZ_longr)/2)t
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = R * c

if (d > 5):                                         #If differnce above given value
  DZ_lat = math.degrees(lat1)                                          #Update the dropzone latitude
  DZ_long = math.degrees(long1)                                       #Update the dropzone longitude

return DZ_lat , DZ_long                                 #Return the dropzone latitude and longitude
