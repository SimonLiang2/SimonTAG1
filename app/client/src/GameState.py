import pygame
from Player import Player
from FlashLightUtils import Boundary,Vector
from MapStates import gen_map;

class GameState:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        self.player = None
        self.map = None
        self.map_img = None
        self.box_resolution = 25
        self.mouseX = 0
        self.mouseY = 0
        self.mouseB = -1
        self.clock = pygame.time.Clock()
        return
    
    def enter(self):
        print(f"Entering: {self.name}")
        self.player = Player(self.state_machine.window_width/2, self.state_machine.window_height/2,5)
        self.map = gen_map(self.box_resolution,self.state_machine.window_width, self.state_machine.window_height)
        self.gen_boundaries()
        self.draw_map()
        return
    
    def leave(self):
        print(f"Leaving: {self.name}")
        return
    
    def get_val_from_map(self,x,y):
        if((0 <= x and x <= len(self.map[0])-1) and (0 <= y and y <= len(self.map)-1)):
            return self.map[y][x]
        return None
          
    def gen_boundaries(self):
        res = self.box_resolution
        #Draw horizontal Lines
        start_vector = None
        end_vector = None
        for i in range(0,len(self.map)):
            start_vector = None
            for j in range(0,len(self.map[0])):
                 val = self.get_val_from_map(j,i)
                 # valid Box
                 if(val == 1 and start_vector == None):
                    if(self.get_val_from_map(j,i-1) == 0 or self.get_val_from_map(j,i+1) == 0):
                        start_vector = Vector(j*res,i*res)
                        end_vector = Vector(start_vector.x+res,start_vector.y)
                 elif(val == 1 and start_vector != None):
                     end_vector = Vector(j*res,i*res)
                 elif(val == 0 and start_vector != None):
                     end_vector = Vector(j*res,i*res)
                     x = int(start_vector.x / res)
                     y = int(start_vector.y / res)
                     if(self.get_val_from_map(x,y-1) == 0):
                        self.player.walls.append(Boundary(start_vector,end_vector))

                     start_bottom_vec = Vector((start_vector.x,start_vector.y+res))
                     end_bottom_vec = Vector((end_vector.x,end_vector.y+res))
                     if(self.get_val_from_map(x,y+1) == 0):
                        self.player.walls.append(Boundary(start_bottom_vec,end_bottom_vec))
                     start_vector = None
                     end_vector = None
                     
            if(start_vector != None):
                x = int(start_vector.x / res)
                y = int(start_vector.y / res)
                if(self.get_val_from_map(x,y-1) == 0):
                    self.player.walls.append(Boundary(start_vector,end_vector))
                start_bottom_vec = Vector((start_vector.x,start_vector.y+res))
                end_bottom_vec = Vector((end_vector.x,end_vector.y+res))
                if(self.get_val_from_map(x,y+1) == 0):
                    self.player.walls.append(Boundary(start_bottom_vec,end_bottom_vec))


        # Draw vertical Lines
        start_vector = None
        end_vector = None
        for i in range(0,len(self.map[0])):
            start_vector = None
            for j in range(0,len(self.map)):
                 val = self.get_val_from_map(i,j)
                 if(val == 1 and start_vector == None):
                     if(self.get_val_from_map(i-1,j) == 0 or self.get_val_from_map(i+1,j) == 0):
                        start_vector = Vector(i*res,j*res)
                        end_vector = Vector(start_vector.x,start_vector.y-res)
                 elif(val == 1 and start_vector != None):
                    end_vector = Vector(i*res,j*res)
                 elif(val == 0 and start_vector != None):
                     end_vector = Vector(i*res,j*res)
                     x = int(start_vector.x / res)
                     y = int(start_vector.y / res)
                     if(self.get_val_from_map(x-1,y) == 0):
                         self.player.walls.append(Boundary(start_vector,end_vector))
                     start_right_vec = Vector((start_vector.x+res,start_vector.y))
                     end_right_vec = Vector((end_vector.x+res,end_vector.y))
                     if(self.get_val_from_map(x+1,y) == 0):
                        self.player.walls.append(Boundary(start_right_vec,end_right_vec))
                     start_vector = None
                     end_vector = None
            if(start_vector != None):
                x = int(start_vector.x / res)
                y = int(start_vector.y / res)
                if(self.get_val_from_map(x-1,y) == 0):
                    self.player.walls.append(Boundary(start_vector,end_vector))
                start_right_vec = Vector((start_vector.x+res,start_vector.y))
                end_right_vec = Vector((end_vector.x+res,end_vector.y))
                if(self.get_val_from_map(x+1,y) == 0):
                    self.player.walls.append(Boundary(start_right_vec,end_right_vec))
                
        return
    
    def draw_map(self):
        res  = self.box_resolution
        self.map_img = pygame.Surface((self.state_machine.window_width, self.state_machine.window_height))
        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[0])):
                 col = (0,0,0)
                 if(self.map[i][j] == 1):
                     col = (255,255,255)
                 self.map_img.fill(col,(j*res,i*res,res,res)) 
        return

    def render(self,window=None):
        res  = self.box_resolution
        background_color = (0, 0, 0)
        window.fill(background_color)
        #window.blit(self.map_img, (0,0))
        index_x = int(self.player.x/res)
        index_y = int(self.player.y/res)
        self.player.render(window)
        # for wall in self.player.walls:
        #     wall.render(window)
        return

    def update(self):
        keys = pygame.key.get_pressed()
        self.mouseX,self.mouseY = pygame.mouse.get_pos()
        self.mouseB = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
        self.player.update(keys,(self.mouseX,self.mouseY,self.mouseB),self.map,self.box_resolution) 
        self.clock.tick(60)  
        return