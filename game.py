from sys import exit

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('complete')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        # be sure to print out the last scene 
        current_scene.enter()
        

        
from dict import *
        
class Map(object):
    
    scenes ={
        'start': Start(),
        'fionaHouse': FionaHouse(),
        'zeldaHome': ZeldaHome(),
        'zeldaWorld': ZeldaWorld(),
        'fight':Fight(),
        'dead': Dead(),
        'underFiona':UnderFiona(),
        'underZelda':UnderZelda(),
        'underFight':UnderFight(),
        'underSchool':UnderSchool(),
        'complete': Complete()
        
        }
        
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

   
the_map = Map('start')
the_game = Engine(the_map)
the_game.play()        