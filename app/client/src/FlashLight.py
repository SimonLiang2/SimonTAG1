import pygame
import numpy as np 
import math 
from FlashLightUtils import Vector
from FlashLightUtils import Ray

def degreeToRadian(degree):
    return (degree / 180) * math.pi; 
def radianToDegree(radian):
    return (radian * 180) / math.pi; 

class FlashLight:
     def __init__(self,x,y,ray_increment):
         self.pos = Vector(x,y)
         self.ray_count = 5  # low resolution
         self.rays = []
         self.divisor = ray_increment

     def update_rays(self,theta):
        self.rays = []
        for i in np.arange(0,self.ray_count,self.divisor):
            degree = radianToDegree(theta) + 4 * i
            self.rays.append( Ray(self.pos,degreeToRadian(degree)))

     def update(self,x,y,theta):
        self.pos = Vector(x,y)
        self.update_rays(theta)

     def flash(self,window,walls,objs=None):
        for ray in self.rays:
            pt = None
            closest = None
            record = 9999 # INFINITY.....
            col = None
            circ = None
            for wall in walls:
                pt = ray.cast(wall)
                if(pt):
                    dist = Vector.dist(self.pos,pt)
                    if(dist < record):
                        record = dist
                        closest = pt
                        col = wall.col

            if (closest):
                blend = pygame.Color(105,100,0,85)
                blend.a = 255
                pygame.draw.line(window,blend,(self.pos.x,self.pos.y),(closest.x,closest.y),2)
                pygame.draw.circle(window,col,(closest.x,closest.y),1)
                if(circ != None):
                    pygame.draw.circle(window,col,(circ.x,circ.y),2)