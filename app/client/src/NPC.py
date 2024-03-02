import pygame

class NPC:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.tagged = False
        self.position = [x,y]
        self.color = (255,255,255)
        self.radius = r
        return
    
    def render(self,window):
        pygame.draw.circle(window, self.color, (self.x,self.y),self.radius,0)
        return
    
    def update(self,tagger_collision_check):
        if (tagger_collision_check):
            self.tagged = True

        self.x = self.position[0]
        self.y = self.position[1]
        
        return

   
        

       