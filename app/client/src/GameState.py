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
        # Draw horizontal Lines
        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[0])):
                 val = self.get_val_from_map(j,i)
                 if(val == 1):
                     pass
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
        window.blit(self.map_img, (0,0))
        index_x = int(self.player.x/res)
        index_y = int(self.player.y/res)
        self.player.render(window)
        for wall in self.player.walls:
            wall.render(window)
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
