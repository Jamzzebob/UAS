import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

Script.ChangeMode("MANUAL")

print 'Resetting Servos'                                #Set all servos to the Neutral position
for chan in range(1,6):
	Script.SendRC(chan,1500,False)
Script.SendRC(3,1000,True)
Script.Sleep(5000)
print 'Done'

print 'Arming Motors'                                   #Arm the Motors
Script.ChangeMode("STABILIZE")
Script.SendRC(3,1000,True)
Script.SendRC(4,2000,True)
cs.messages.Clear()
Script.WaitFor('ARMING MOTORS', 20000)
print 'Motors Armed'
Script.SendRC(4,1500,true)                              #Return Rudder to Neutral position

Script.ChangeMode("MANUAL")

Script.ChangeMode("AUTO")

DZ_lat = math.radians(-35.361259)											#Will be imported from datafile eventually
DZ_long = math.radians(149.162025)										#Will be imported from datafile eventually

while True:																						
    Script.Sleep(100)
    from Targetlocation import targetloc
    DZ_lat,DZ_long = targetloc(DZ_lat,DZ_long)
    wpno = cs.wpno
    int(wpno)
    if (wpno == 4):
        break

x = 80
y = 100
dist = math.sqrt((x**2)+(y**2))
print(dist)
theta = math.atan2(x,y)
print(theta)
R = 6371000

DP_lat = math.degrees(math.asin(math.sin(DZ_lat)*math.cos(dist/R) + math.cos(DZ_lat)*math.sin(dist/R)*math.cos(theta)))
print(DP_lat)
#Calculate the Latitude of the Droppoint
DP_long = math.degrees(DZ_long + math.atan2(math.sin(theta)*math.sin(dist/R)*math.cos(DZ_lat) , math.cos(dist/R)-math.sin(DZ_lat)*math.sin(DP_lat)))
print(DP_long)
#Calculate the Longitude of the Droppoint

item = MissionPlanner.Utilities.Locationwp()
Locationwp.lat.SetValue(item,DP_lat)           # sets latitude
Locationwp.lng.SetValue(item,DP_long)          # sets longitude
Locationwp.alt.SetValue(item,30)               # sets altitude

print("DP Loaded")

while True:
    Script.Sleep(100)
    wpno = cs.wpno
    int(wpno)
    if (wpno == 7):
        break

MAV.setGuidedModeWP(item)                       # tells UAS to go to the set lat/long/alt
print("Navigating DP")

Script.Sleep(60000)

print("Resuming Mission")
Script.ChangeMode("AUTO")

  
  while true                                  #Confirm that the UAS has stopped moving
     speed= cs.groundspeed
     If speed = 0
         break

Script.SendRC(3,1000,True)                    #Disarm the Motors
Script.WaitFor('DISARMING MOTORS', 20000)
print 'Motors Disarmed'
break

print 'Mission Complete'                      #Main script ends
