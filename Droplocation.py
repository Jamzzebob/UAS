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

def dloc(wspd,wdir,alt,v,p,r):                                     #Define Function dloc()
  heading = wdir
  wdir = wdir+180

  if (wdir > 360):
    wdir = wdir-360

  wx = wspd * math.sin(math.radians(wdir))        #Calculate component of wind in the x direction
  wy = wspd * math.cos(math.radians(wdir))        #Calculate component of wind in the y direction

  from Scripts.Payload import density                           #Import all variable and functions from the payload file
  from Scripts.Payload import m                                                         #Import payload mass
  from Scripts.Payload import A1                                                   #Import payload face area 1
  from Scripts.Payload import A2                                                    #Import payload face area 2
  from Scripts.Payload import A3                                                    #Import payload face area 3
  from Scripts.Payload import cd
  
  rho = density(alt,p)                                 #Call the density Function to work out the air density

  sz = 0                                          #Initilise the displacement in the z directon
  sy = 0                                          #Initilise the displacement in the y directon
  sx = 0                                          #Initilise the displacement in the x directon
  t1 = 0                                          #Initilise the fall time
  t2 = 0                                          #Initilise the counter
  t3 = 0                                          #Initilise the counter
  vz = 0                                          #Initilise Velocity in the z direction0k
  vx = v * math.sin(math.radians(heading))        #Initilise Velocity in the x direction
  vy = v * math.cos(math.radians(heading))        #Initilise Velocity in the y direction
 
  while ( sz  <  alt ):                            #Calculate fall time
    t1= t1 + 0.01
    D = 0.5*rho*A1*cd*vz**2
    a = 9.81-(D/m)
    sz = sz + (vz*(0.01) + 0.5*a*(0.01**2))
    vz = vz + a*(0.01)

  while ( t2 < t1 ):                               #Calculate displacement in the x direction
    t2 = t2 + 0.01
    D = 0.5*rho*A2*cd*(vx - wx)**2
    a = (D)/m
    a = math.copysign(a,-vx)
    sx = sx + (vx*0.01) + 0.5*a*(0.01**2)
    vx = vx + a*0.01

  while  ( t3 < t1 ):                              #Calculate displacement in the y direction
    t3 = t3 + 0.01
    D = 0.5 * rho * A3 * cd * (vy - wy)**2
    a = (D)/m
    a = math.copysign(a,-vy)
    sy = sy + (vy*0.01) + 0.5*a*(0.01**2)
    vy = vy + a*0.01

  D_angle = heading + 90 
  if (D_angle > 360):
    D_angle = D_angle - 360

  sx = -sx
  sy = -sy

  x = -r * math.sin(math.radians(D_angle))
  y = -r * math.cos(math.radians(D_angle))

  sx = sx + x
  sy = sy + y

  return sx,sy                                    #Return the x and y position of the droppoint relative to the dropzone (m)
