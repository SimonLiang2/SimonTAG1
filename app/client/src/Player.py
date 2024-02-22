import pygame
class Player:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.color = (255,255,255)
        self.velocity = [0,0]
        self.acceleration = 0.002
        self.radius = r
        self.max_speed = 0.2
        self.friction_mag = 10
        return

    def update(self,keys,map_data,res_x,res_y):
        self.process_movement(keys,map_data,res_x,res_y)
        return

    def process_movement(self,keys,map_data,res_x,res_y):
        key_hit = False
        if(keys[pygame.K_a] and (0 + self.radius) < self.x):
                self.velocity[0] -= self.acceleration
                if(self.velocity[0] < -self.max_speed):
                      self.velocity[0] = -self.max_speed
                key_hit = True
        elif(keys[pygame.K_d] and self.x < (600 - self.radius)):
                self.velocity[0] += self.acceleration
                if(self.velocity[0] > self.max_speed):
                      self.velocity[0] = self.max_speed
                key_hit = True

        if(keys[pygame.K_w] and (0 + self.radius) < self.y):
                self.velocity[1] -= self.acceleration
                if(self.velocity[1] < -self.max_speed):
                      self.velocity[1] = -self.max_speed
                key_hit = True
                
        elif(keys[pygame.K_s] and self.y < (600 - self.radius)):
                self.velocity[1] += self.acceleration
                if(self.velocity[1] > self.max_speed):
                      self.velocity[1] = self.max_speed
                key_hit = True

        if(not key_hit):
              if(self.velocity[0] < 0):
                    self.velocity[0] += self.acceleration * self.friction_mag
                    if(self.velocity[0] >= 0):
                          self.velocity[0] = 0
              if(self.velocity[0] > 0):
                    self.velocity[0] -= self.acceleration * self.friction_mag
                    if(self.velocity[0] <= 0):
                          self.velocity[0] = 0

              if(self.velocity[1] < 0):
                    self.velocity[1] += self.acceleration * self.friction_mag
                    if(self.velocity[1] >= 0):
                          self.velocity[1] = 0
              if(self.velocity[1] > 0):
                    self.velocity[1] -= self.acceleration * self.friction_mag
                    if(self.velocity[1] <= 0):
                          self.velocity[1] = 0
   
        self.x += self.velocity[0]
        index_x = int(self.x/res_x)
        index_y = int(self.y/res_y)
        if(map_data[index_x][index_y] == (255,255,255)):
              self.x -= self.velocity[0]

        self.y += self.velocity[1]
        index_x = int(self.x/res_x)
        index_y = int(self.y/res_y)
        if(map_data[index_x][index_y] == (255,255,255)):
              self.y -= self.velocity[1]

    def render(self,window):
        pygame.draw.circle(window, self.color, (self.x,self.y),self.radius,0)
        return
    
# Show becky and then delete
#       if keys[pygame.K_a] and (0 + self.player.radius) < self.player.x:
        #         self.player.x -= self.player.velocity
                
        # if keys[pygame.K_d] and self.player.x < (600 - self.player.radius):
        #         self.player.x += self.player.velocity

        # if keys[pygame.K_w] and (0 + self.player.radius) < self.player.y:
        #         self.player.y -= self.player.velocity
                
        # if keys[pygame.K_s] and self.player.y < (600 - self.player.radius):
        #         self.player.y += self.player.velocity