#This Module defines a function which calculates the position of the drop point relative to the dropzone
#Note Postive x represents North, Positive y Represents South and Positive z represents distance above ground 

import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

def dloc():                                     #Define Function dloc()

wspd = cs.wind_vel                              #Pull Wind Speed (m)
wdir = cs.wind_dir                              #Pull Wind DIrection (degrees from north)
alt = cs.alt                                    #Pull Altitude (m)

wx = wspd * math.cos(math.radians(wdir))        #Calculate component of wind in the x direction
wy = wspd * math.sin(math.radians(wdir))        #Calculate component of wind in the y direction

from payload import *                           #Import all variable and functions from the payload file
rho = density()                                 #Call the density Function to work out the air density

sz = 0                                          #Initilise the displacement in the z directon
sy = 0                                          #Initilise the displacement in the y directon
sx = 0                                          #Initilise the displacement in the x directon
t1 = 0                                          #Initilise the fall time
t2 = 0                                          #Initilise the counter
t3 = 0                                          #Initilise the counter
heading = cs.yaw                                #Pull UAS heading (degrees from North)
V = cs.groundspeed                              #Pull UAS Velocity
vz = 0                                          #Initilise Velocity in the z direction
vx = v * math.cos(math.radians(heading))        #Initilise Velocity in the x direction
vy = v * math.sin(math.radians(heading))        #Initilise Velocity in the y direction

while ( sz  <  alt )                            #Calculate fall time
  t= t + 0.01
  D = 0.5*rho*A1*cd*vz^2
  a = 9.81-(D/m)
  sz = sz + (vz*(0.01) + 0.5*a*(0.01^2)
  vz = vz + a*(0.01)

while ( t2 < t1 )                               #Calculate displacement in the x direction
t2 = t2 + 0.01;
D = 0.5*rho*A2*cd*(vx-wx)^2
a = (-D)/m
sx = sx + (vx*0.01) + 0.5*a*(0.01^2)
vx = vx + a*0.01

while  ( t3 <=t1 )                              #Calculate displacement in the y direction
t3= t3 + 0.01
D = 0.5 * rho * A3 * cd * (abs(vy)-abs(wy))^2
a = D/m
a = math.copysign(a , -(vy-wy))
sy = sy + (vy*0.01) + 0.5*a*(0.01^2)
vy = vy + a*0.01

return sx,sy                                    #Return the x and y position of the droppoint relative to the dropzone (m)
