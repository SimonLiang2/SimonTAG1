import pygame
from FlashLight import FlashLight
from MapStates import find_spawn_point;

class NPC:
    def __init__(self,x,y,r,col=(255,255,255)):
        self.x = x
        self.y = y
        self.position = [x,y]
        self.color = col
        self.radius = r
        return
    
    def get_new_position(self,map_data,resolution):
        valid_x,valid_y = find_spawn_point(map_data,resolution)
        self.x = valid_x
        self.y = valid_y
        return

    def render(self,window):
        pygame.draw.circle(window, self.color, (self.x,self.y),self.radius,0)
        return
    
    def update(self):
        
        return

   
        

       