import pygame
from FlashLight import FlashLight

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
        self.color = (255,255,255)
        if (self.tagged):
            self.color = (219,165,255)
        
        self.collide = pygame.Rect(self.x,self.y,self.radius,self.radius)

        pygame.draw.circle(window, self.color, (self.x,self.y),self.radius,0)
        return
    
    def update(self):
        

        self.x = self.position[0]
        self.y = self.position[1]
        
        return

   
        

       