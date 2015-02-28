#This Module Defines the Function target() which can be called to calculate the coordinates of the dropzone

import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

m = 1                                                         #Define payload mass
h = 0.22                                                         #Define payload height
w = 0.15                                                         #Define payload width
d = 0.08                                                         #Define payload depth
A1 = w*d                                                    #Calculate payload face area 1
A2 = h*d                                                    #Calculate payload face area 2
A3 = h*w                                                    #Calculate payload face area 3
cd = 1.03                                                       #Define payload drag coefficient

def density(alt,p):                                         #Define the function to calcualate air density                                                #Pull altitude
    T0 =288.15                                                  #Temperture at sea level
    R = 8.31447                                                 #Universal gas constant
    M = 0.0289644                                               #Molar mass of dry air
    T = T0 -( 0.0065*alt)                                   #Calculate temperture at flying altitude
    rho = (p*M)/(T*R)                                           #Calcualte the air density
    return rho                                                  #Return the air density
