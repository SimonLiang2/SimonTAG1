import pygame
import math
from FlashLight import FlashLight

# Vector utilities
vec_up = [0,-1]
vec_down = [0,1]
vec_left = [1,0]
vec_right = [-1,0]
vecs = [vec_up,vec_down,vec_left,vec_right]

def add(vec_a,vec_b):
    return [vec_a[0]+vec_b[0],vec_a[1]+vec_b[1]]
def sub(vec_a,vec_b):
    return [vec_a[0]-vec_b[0],vec_a[1]-vec_b[1]]
def mag(vec):
    return math.sqrt((vec[0]*vec[0])  + (vec[1]*vec[1]))
def mult(vec,a):
    return [vec[0]*a,vec[1]*a]
def norm(vec):
    m = mag(vec)
    if(m == 0):
        m = 1
    return [vec[0]/m,vec[1]/m]
def set_mag(vec,a):
    return mult(norm(vec),a)

# Global definitions
WALL = 1

class Player:
    def __init__(self,x,y,r):
        self.tagged = False
        self.x = x
        self.y = y
        self.position = [x,y]
        self.color = (0,0,255)
        self.velocity = [0,0]
        self.acceleration = 0.5
        self.radius = r
        self.max_speed = 3
        self.friction_mag = 0.5
        self.flash_light = FlashLight(x,y,0.01)
        self.mouseDown = False
        return
    
    def render(self,window,walls,objects):
        
        if(self.mouseDown):
            self.flash_light.flash(window,walls,objects)

        self.color = (0,0,255)
        if(self.tagged):
            self.color = (255,255,0)

        pygame.draw.circle(window, self.color, (self.x,self.y),self.radius,0)
        a = set_mag(self.velocity,self.radius*2)
        pygame.draw.line(window,(255,0,0),(self.x,self.y),
                                          (self.x+a[0],self.y+a[1]),1)
        return
    
    def update(self,keys,mouse,map_data,res,objs=None):
        
        dx = mouse[0] - (self.position[0])
        dy = mouse[1] - (self.position[1])
        theta = math.atan2(dy,dx)

        self.mouseDown = mouse[2][0]

        if(self.mouseDown):
            self.flash_light.update(self.position[0],self.position[1],theta)  
    
        wasd = [keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d]]
        self.process_movement(wasd,map_data,res)
        self.x = self.position[0]
        self.y = self.position[1]
     
        return

    def process_movement(self,keys,map_data,res):
        #         W           A           S         D
        key_hit = keys[0] or keys[1] or keys[2] or keys[3] 
        if(key_hit):
            if(keys[0]):
                self.velocity[1] -= self.acceleration
            if(keys[1]):
                self.velocity[0] -= self.acceleration
            if(keys[2]):
                self.velocity[1] += self.acceleration
            if(keys[3]):
                self.velocity[0] += self.acceleration
            if(mag(self.velocity) > self.max_speed):
                self.velocity = set_mag(self.velocity,self.max_speed)
        else:
            #apply friction
            self.velocity[0] += (self.acceleration * self.friction_mag) if (self.velocity[0] < 0) else (-self.acceleration * self.friction_mag)
            self.velocity[1] += (self.acceleration * self.friction_mag) if (self.velocity[1] < 0) else (-self.acceleration * self.friction_mag)
            if(abs(self.velocity[0]) <= 0.5): 
                 self.velocity[0] = 0
            if(abs(self.velocity[1]) <= 0.5): 
                 self.velocity[1] = 0

        self.position[0] += self.velocity[0] 
        self.check_collision(map_data,res)

        self.position[1] += self.velocity[1]
        self.check_collision(map_data,res)
        

    def check_collision(self,map,res):
        for i in range(len(vecs)):
            t = mult(vecs[i],self.radius-2)
            a = add(self.position,t)
            index_x = int((a[0]) / res)
            index_y = int((a[1]) / res)
            
            try:
                on = map[index_y][index_x]
                if(on == WALL):
                    self.position = add(self.position,mult(t,-1))
                    return False
            except:
                pass
                 
        return True      