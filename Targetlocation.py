import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

def targetloc(DZ_lat,DZ_long,cslat,cslng):                          #Define the function
  
  x,y = 0,0                                               #Initilise x and y
  t = 0
  from Scripts.ImageRecognition import imrec                      #Import the image recognition

  x, y = imrec(DZ_lat,DZ_long,cslat,cslng)
  
  lat = math.radians(cslat)                                            #Pull the currrent UAS latitude
  lon = math.radians(cslng)                                           #Pull the current UAS longitude
  
  dist=math.sqrt((x**2)+(y**2))                             #Calcualte the distance to the dropzone
  theta = (math.atan2(x,y)+(2*math.pi)) % (2*math.pi)                                 #Calculate the angle to the drop zone
  R = 6371000                                             #Radius of the Earth
  
  lat1 = ( math.asin((math.sin(lat) * math.cos(dist/R))+(math.cos(lat)*math.sin(dist/R)*math.cos(theta))))
  #Calculate the latitude of the dropzone
  long1 = (lon +math.atan2(math.sin(theta)*math.sin(dist/R)*math.cos(lat) , math.cos(dist/R)-math.sin(lat)*math.sin(lat1)))
  #Calculate the longitude of the dropzone
  
  DZ_latr = math.radians(DZ_lat)
  DZ_longr = math.radians(DZ_lat)
  
  a = math.sin((lat1-DZ_latr)/2) * math.sin((lat1-DZ_latr)/2) + math.cos(DZ_latr) * math.cos(lat1) * math.sin((long1-DZ_longr)/2) * math.sin((long1-DZ_longr)/2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  d = R * c
  
  if (d > 5):                                         #If differnce above given value
    DZ_lat = math.degrees(lat1)                                          #Update the dropzone latitude
    DZ_long = math.degrees(long1)                                       #Update the dropzone longitude
  
  print(DZ_lat)
  print(DZ_long)
  
  return DZ_lat , DZ_long                                 #Return the dropzone latitude and longitude
