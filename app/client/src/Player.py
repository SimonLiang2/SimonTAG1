import pygame
import math

# Vector utilities
def mag(vec):
    return math.sqrt((vec[0]*vec[0])  + (vec[1]*vec[1]))
def  mult(vec,a):
    return [vec[0]*a,vec[1]*a]
def norm(vec):
    return [vec[0]/mag(vec),vec[1]/mag(vec)]
def set_mag(vec,a):
    return mult(norm(vec),a)

# Global definitions
WALL = (255,255,255)

class Player:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.position = [x,y]
        self.color = (0,0,255)
        self.velocity = [0,0]
        self.acceleration = 0.002
        self.radius = r
        self.max_speed = 0.2
        self.friction_mag = 1/2
        return
    
    def render(self,window):
        pygame.draw.circle(window, self.color, (self.x,self.y),self.radius,0)
        return
    
    def update(self,keys,map_data,res):
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
            if(abs(self.velocity[0]) <= 0.02): 
                 self.velocity[0] = 0
            if(abs(self.velocity[1]) <= 0.02): 
                 self.velocity[1] = 0
       
        self.position[0] += self.velocity[0]
        self.check_collision(map_data,res,0)
        self.position[1] += self.velocity[1]
        self.check_collision(map_data,res,1)
      
    def check_collision(self,map,res,dir):
        index_x = int(self.position[0]/res)
        index_y = int(self.position[1]/res)
        on = map[index_y][index_x]

        if(on == WALL):
            self.position[dir] -= self.velocity[dir] 
            return False
        
        return True      
    
# Show becky and then delete
#       if keys[pygame.K_a] and (0 + self.player.radius) < self.player.x:
        #         self.player.x -= self.player.velocity
                
        # if keys[pygame.K_d] and self.player.x < (600 - self.player.radius):
        #         self.player.x += self.player.velocity

        # if keys[pygame.K_w] and (0 + self.player.radius) < self.player.y:
        #         self.player.y -= self.player.velocity
                
        # if keys[pygame.K_s] and self.player.y < (600 - self.player.radius):
        #         self.player.y += self.player.velocity