##import sys
##sys.path.insert(0,'C:/Users/Metsane/Documents/Python/ZeldaGame/dict.py')
##from dict.py import Map
import dict
from game import *


##class Start(Scene):
##    def enter(self):
  ##      print("\tWelcome to hove groove, your city's being terrorised by the evil Zelda")
    ##  print("\tMurded FIONA's dungeon, Evil ZELDA's childhood home, Hove groove's high school?")
      ##  choice = input("> ")
      ##  if choice == "FIONA" or choice == "fiona":
        ##    return 'fionaHouse'
##        elif choice == "ZELDA" or choice == "zelda":
  ##          return 'zeldaHome'
  ##      elif choice == "high school":
  ##          raise ValueError("No!")
  ##      else:
  ##          print("????? And what's that? ?????\b")
  ##          return 'start'

running = Start()
running.enter()