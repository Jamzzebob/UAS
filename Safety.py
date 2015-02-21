import sys
import math
import time
import clr
import subprocess
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp

p = subprocess.Popen([sys.executable, 'Main.py'])                   #Begin the main script

while true                                                          #Continually check for manual mode
  time.sleep(0.1)
  mode = cs.mode
  if mode="MANUAL"
    break

p.terminate()                                                       #Terminate the main script

Script.ChangeMode("MANUAL")                                         #Set the Mode to Manual

print("Warning Aircraft Under Manual Control")                      #Print Warning and End
