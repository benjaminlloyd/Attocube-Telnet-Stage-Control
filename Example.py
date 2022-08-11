from Control import Control
from Connect import Connect

stages=Control(Connect('192.168.7.10').tn)
stages.turnon()
stages.roomtemp()
stages.move(3,-1,20,280) #axis, steps, voltage, frequency
stages.turnoff()
