from Control import Control
from Connect import Connect

stages=Control(Connect('192.168.7.10').tn)
stages.turnon()
stages.turnoff()