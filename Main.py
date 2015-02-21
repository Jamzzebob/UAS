import sys
import math
import time
import clr
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

while cs.lat == 0                                       #Wait for GPS to connect
 print 'Waiting for GPS'
 Script.Sleep(1000)
print 'Got GPS'

print 'Resetting Servos'                                #Set all servos to the Neutral position
for chan in range(1,6)
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

from Waypoint import *
print 'Waypoints Set'                                   #Import the waypoint data

#Here Will be code for the plane to take-off

#Navigate the dropzone
Locationwp.lat.SetValue(item,DZ_lat)              # sets latitude
Locationwp.lng.SetValue(item,DZ_long)             # sets longitude
Locationwp.alt.SetValue(item,alt)                 # sets altitude
MAV.setGuidedModeWP(item)                         # tells UAS to go to the set lat/long/alt
print 'Navigating Drop Zone'

from Targetlocation import targetloc              #Import the target location function

DZ_lat,DZ_long = targetloc(DZ_lat,DZ_long)        #Update the Dropzone coordinates

While True:                                       #Check arrival at dropzone
bearingerror= cs.ber_error
dis= cs.wp_dist
if (dis <= WaypointTolerence):
if (dis <= bearingerror):
break

#Navigate Waypoint A
Locationwp.lat.SetValue(item,WPA_lat)             # sets latitude
Locationwp.lng.SetValue(item,WPA_long])           # sets longitude
Locationwp.alt.SetValue(item,alt)                 # sets altitude
MAV.setGuidedModeWP(item)                         # tells UAS to go to the set lat/long/alt
Print 'Navigating Waypoint A'

While True:                                       #Check Arrival at waypoint A
bearingerror= cs.ber_error
dis= cs.wp_dist
if (dis <= WaypointTolerence):
if (dis <= bearingerror):
break

#Navigate waypoint B
Locationwp.lat.SetValue(item,WPB_lat)           # sets latitude
Locationwp.lng.SetValue(item,WPB_long)          # sets longitude
Locationwp.alt.SetValue(item,alt)               # sets altitude
MAV.setGuidedModeWP(item)                       # tells UAS to go to the set lat/long/alt
Print 'Navigating Waypoint B'

While True:                                     #Check arrival at waypoint B
bearingerror= cs.ber_error
dis= cs.wp_dist
if (dis <= WaypointTolerence):
if (dis <= bearingerror):
break

#Navigate waypoint C
Locationwp.lat.SetValue(item,WPC_lat)           # sets latitude
Locationwp.lng.SetValue(item,WPC_long)          # sets longitude
Locationwp.alt.SetValue(item,alt)               # sets altitude
MAV.setGuidedModeWP(item)                       # tells UAS to go to the set lat/long/alt
Print 'Navigating Waypoint C'

While True:                                     #Check Arrival at waypoint C
bearingerror= cs.ber_error
dis= cs.wp_dist
if (dis <= WaypointTolerence):
if (dis <= bearingerror):
break

#Navigate to the dropzone
Locationwp.lat.SetValue(item,DZ_lat)            # sets latitude
Locationwp.lng.SetValue(item,DZ_lomg)           # sets longitude
Locationwp.alt.SetValue(item,alt)               # sets altitude
MAV.setGuidedModeWP(item)                       # tells UAS to go to the set lat/long/alt
Print 'Navigating Drop Zone'

From targeting import target                    #Import the targeting function
lat , long = 0 , 0                              #Initilize the latitude and the longitude

while true                                      #Get the droppoint latitude and longitde
  lat , long = target() 
  Script.Sleep(1000)
  if ( lat , long != 0 , 0)
    break
  dis = cs.wp_dist
  if( dis <= 20)                              #If the target has not been recognised within a certain distance
    #The image recognition will deliver the payload purely by GPS and wind speed calculation
    #As yet to be implimented

#Navigate to the droppoint
Locationwp.lat.SetValue(item,lat)             # sets latitude
Locationwp.lng.SetValue(item,long)            # sets longitude
Locationwp.alt.SetValue(item,alt)             # sets altitude
MAV.setGuidedModeWP(item)                     # tells UAS to go to the set lat/long/alt
Print 'Navigating Drop Point'

While True:                                   #Chech if arrived at droppoint
bearingerror= cs.ber_error
dis= cs.wp_dist
if (dis <= DropTolerence):
if (dis <= bearingerror):
break

Script.SendRC(5, 2000, True)                  #Release the payload      
Print 'Payload 1 released'

#Here the aircraft will reposition to deliver the second payload

#Navigate to the dropzone agian
Locationwp.lat.SetValue(item,DZ_lat)          # sets latitude
Locationwp.lng.SetValue(item,DZ_long)         # sets longitude
Locationwp.alt.SetValue(item,alt)             # sets altitude
MAV.setGuidedModeWP(item)                     # tells UAS to go to the set lat/long/alt
Print 'Navigating Drop Zone'

while true                                      #Get the droppoint latitude and longitde
  lat , long = target() 
  Script.Sleep(1000)
  if ( lat , long != 0 , 0)
    break
  dis = cs.wp_dist
  if( dis <= 20)                              #If the target has not been recognised within a certain distance
    #The image recognition will deliver the payload purely by GPS and wind speed calculation
    #As yet to be implimented

#Navigate to droppoint
Locationwp.lat.SetValue(item,lat)             # sets latitude
Locationwp.lng.SetValue(item,long)            # sets longitude
Locationwp.alt.SetValue(item,alt)             # sets altitude
MAV.setGuidedModeWP(item)                     # tells UAS to go to the set lat/long/alt
Print 'Navigating Drop Point'

While True:                                   #Check arrived at droppoint
bearingerror= cs.ber_error
dis= cs.wp_dist
if (dis <= DropTolerence):
if (dis <= bearingerror):
break

Script.SendRC(6, 2000, True)                  #Release payload 2
Print 'Payload 2 released'

#The UAS must return to a position and then postion it's self so that it can land within the 30x10m box

while true                                    #Land the UAS
 dish = cs.DistToHome
 If dish = Landingdistance
  Script.ChangeMode("LAND") 
# changes Mode to "Land"
  print 'Landing'
  break
  
  while true                                  #Confirm that the UAS has stopped moving
     speed= cs.groundspeed
     If speed = 0
         break

Script.SendRC(3,1000,True)                    #Disarm the Motors
Script.WaitFor('DISARMING MOTORS', 20000)
print 'Motors Disarmed'
break

print 'Mission Complete'                      #Main script ends
