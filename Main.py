import sys
sys.path.append('Users\James\Desktop\Scripts')
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp
Script.ChangeMode("MANUAL")

print("Resetting Servos")                                #Set all servos to the Neutral position
for chan in range(1,6):
        Script.SendRC(chan,1500,False)
Script.SendRC(3,1000,True)
Script.Sleep(2000)
print("Done")

print("Arming Motors")                                   #Arm the Motors
MAV.doARM(1)
print("Motors Armed")

Script.ChangeMode("MANUAL")

Script.ChangeMode("AUTO")

from Scripts.Waypoint import DZ_lat
from Scripts.Waypoint import DZ_long
from Scripts.Waypoint import r

while True:
        Script.Sleep(100)
        from Scripts.Targetlocation import targetloc
        cslat = cs.lat
        cslng = cs.lng
        DZ_lat,DZ_long = targetloc(DZ_lat,DZ_long,cslat,cslng)
        wpno = cs.wpno
        int(wpno)
        if (wpno == 4):
                break

while True:
        Script.Sleep(100)
        wpno = cs.wpno
        int(wpno)
        if (wpno == 7):
                break

from Scripts.Droplocation import dloc

wspd = cs.wind_vel
wdir = cs.wind_dir
alt = cs.alt
v = cs.groundspeed
p = cs.press_abs

x,y = dloc(wspd,wdir,alt,v,p,r)
dist = math.sqrt((x**2)+(y**2))
theta = math.atan2(x,y)
R = 6371000
DZ_lat = math.radians(DZ_lat)
DZ_long = math.radians(DZ_long)


DP_lat = math.asin(math.sin(DZ_lat)*math.cos(dist/R) + math.cos(DZ_lat)*math.sin(dist/R)*math.cos(theta))
#Calculate the Latitude of the Droppoint
DP_long = DZ_long + math.atan2(math.sin(theta)*math.sin(dist/R)*math.cos(DZ_lat) , math.cos(dist/R)-math.sin(DZ_lat)*math.sin(DP_lat))
#Calculate the Longitude of the Droppoint
DP_lat = math.degrees(DP_lat)
DP_long = math.degrees(DP_long)

item = MissionPlanner.Utilities.Locationwp()
Locationwp.lat.SetValue(item,DP_lat)           # sets latitude
Locationwp.lng.SetValue(item,DP_long)          # sets longitude
Locationwp.alt.SetValue(item,30)               # sets altitude

print("DP Loaded")



if (cs.mode == "MANUAL"):
        print("Mission Failed due to Manual Override")
        sys.exit()
else:
        MAV.setGuidedModeWP(item)                       # tells UAS to go to the set lat/long/alt
        print("Navigating DP")


while True:
        wpdist = cs.wp_dist
        if (wpdist < 70):
                break

while True:
        TB = cs.groundcourse
        if (cs.mode == "MANUAL"):
                print("Mission Failed due to Manual Override")
                sys.exit()
        if (TB < (wdir+4)):
                if (TB > (wdir-4)):
                        Script.SendRC(5,2000,True)
                        print("Payload 1 Released")
                        break

Script.Sleep(3000)

while True:
        TB = cs.groundcourse
        if (cs.mode == "MANUAL"):
                print("Mission Failed due to Manual Override")
                sys.exit()
        if (TB < (wdir+4)):
                if (TB > (wdir-4)):
                        Script.SendRC(6,2000,True)
                        print("Payload 2 Released")
                        break

Script.Sleep(3000)

if (cs.mode == "MANUAL"):
        print("Mission Failed due to Manual Override")
        sys.exit()
else:
        print("Resuming Mission")
        Script.ChangeMode("AUTO")
  
while True:                                #Confirm that the UAS has stopped moving
        speed= cs.groundspeed
        if (speed == 0):
                print("Landed")
                break

print("Disarming motors")              
MAV.doARM(0)
print("Motors Disarmed")

print("Mission Complete")              #Main script ends
