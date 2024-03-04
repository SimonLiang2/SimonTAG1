import pygame
import numpy as np 
import math 
from FlashLightUtils import Vector
from FlashLightUtils import Ray
from FlashLightUtils import Circle

def degreeToRadian(degree):
    return (degree / 180) * math.pi; 
def radianToDegree(radian):
    return (radian * 180) / math.pi; 

class FlashLight:
     def __init__(self,x,y,ray_increment):
         self.pos = Vector(x,y)
         self.ray_count = 2  # low resolution
         self.rays = []
         self.divisor = ray_increment
         self.draw_circle = False
         self.circles = []

     def update_rays(self,theta):
        self.rays = []
        for i in np.arange(0,self.ray_count,self.divisor):
            degree = radianToDegree(theta) + 4 * i * 3
            self.rays.append( Ray(self.pos,degreeToRadian(degree)))

     def update(self,x,y,theta):
        self.pos = Vector(x,y)
        self.update_rays(theta)

     def flash(self,window,walls,objs=None):
        self.draw_circle = False
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
                        col = wall.color
            if(objs != None):
                        for obj in objs:
                            c = Circle(obj.x,obj.y,obj.radius,obj.color)
                            pt = ray.cast_circle(c)
                            if(pt):
                                dist = Vector.dist(self.pos,pt[0])
                                if(dist < record):
                                    record = dist
                                    closest = pt[0]
                                    circ = pt[1]
                                    col = c.color

            if (closest):
                line_size = 4
                circle_size = 3
                #color of the flashlight
                blend = pygame.Color(105,100,0,85)
                blend.a = 255
                if(circ == None):
                    pygame.draw.line(window,blend,(self.pos.x,self.pos.y),(closest.x,closest.y),line_size)
                if(circ != None):
                    circle_size = 1
                    line_size = 3
                    pygame.draw.line(window,blend,(self.pos.x,self.pos.y),(closest.x,closest.y),line_size)
                    self.draw_circle = True
                    if(len(self.circles) < 600):
                        self.circles.append([circ.x,circ.y,col,circle_size])
                        self.circles.append([closest.x,closest.y,col,circle_size])
                    pygame.draw.circle(window,col,(circ.x,circ.y),circle_size)
                pygame.draw.circle(window,col,(closest.x,closest.y),circle_size)

        if(not self.draw_circle):
            self.circles = []      
        print(len(self.circles))  
        for point in self.circles:
            pygame.draw.circle(window,point[2],(point[0],point[1]),point[3])
