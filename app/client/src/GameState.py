import pygame
from Player import Player
from MapStates import gen_map;
class GameState:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        self.player = None
        self.res_x = None
        self.res_y = None
        self.map = None
        self.map_img = None
        self.box_resolution = 25
        return
    
    def enter(self):
        print(f"Entering: {self.name}")
        self.player = Player(self.state_machine.window_width/2, self.state_machine.window_height/2,5)
        self.map = gen_map(self.box_resolution,self.state_machine.window_width, self.state_machine.window_height)
        self.draw_map()
        return
    
    def leave(self):
        print(f"Leaving: {self.name}")
        return
    
    def draw_map(self):
        res  = self.box_resolution
        self.map_img = pygame.Surface((self.state_machine.window_width, self.state_machine.window_height))
        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[0])):
                 self.map_img.fill(self.map[i][j],(j*res,i*res,res,res)) 
        return

    def render(self,window=None):
        res  = self.box_resolution
        background_color = (0, 0, 0)
        window.fill(background_color)
        window.blit(self.map_img, (0,0))
        index_x = int(self.player.x/res)
        index_y = int(self.player.y/res)
        pygame.draw.rect(window,(255,0,0),(index_x*res,index_y*res,res,res))
        self.player.render(window)
        pygame.display.update()
        return

    def update(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
        self.player.update(keys,self.map,self.box_resolution)       
        return