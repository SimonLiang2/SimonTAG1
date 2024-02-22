import pygame
from Player import Player
from MapStates import gen_map;
class GameState:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        self.player = Player(300,300,5)
        self.res_x = None
        self.res_y = None
        self.map = None
        self.map_img = None
        return
    
    def enter(self):
        print(f"Entering: {self.name}")
        self.res_x = int(self.state_machine.window_width/24)
        self.res_y = int(self.state_machine.window_height/24)
        self.map = gen_map(self.res_x,self.res_y)
        self.draw_map()
        return
    
    def leave(self):
        print(f"Leaving: {self.name}")
        return
    
    def draw_map(self):
        self.map_img = pygame.Surface((600, 600))
        for i in range(0,self.res_y):
            for j in range(0,self.res_x):
                 self.map_img.fill(self.map[i][j],(i*self.res_y,j*self.res_x,self.res_x,self.res_y)) 
        return

    def render(self,window=None):
        background_color = (0, 0, 0)
        window.fill(background_color)
        window.blit(self.map_img, (0,0))
        index_x = int(self.player.x/self.res_x)
        index_y = int(self.player.y/self.res_y)
        pygame.draw.rect(window,(255,0,0),(index_x*self.res_x,index_y*self.res_y,self.res_x,self.res_y))
        self.player.render(window)
        pygame.display.update()
        return

    def update(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
        self.player.update(keys,self.map,self.res_x,self.res_y)       
        return