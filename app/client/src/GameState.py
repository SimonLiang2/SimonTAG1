import pygame
import random as r
import math 
from Player import Player
from NPC import NPC
from FlashLightUtils import Boundary,Vector,Circle
from MapStates import gen_map, find_spawn_point;
from CreateMaps import choose_random_map, choose_map, get_last_map

class GameState:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        self.player = None
        self.map = None
        self.map_img = None
        self.box_resolution = 50
        self.mouseX = 0
        self.mouseY = 0
        self.mouseB = -1
        self.clock = pygame.time.Clock()
        self.debug_mode = False
        self.score = 0
        self.walls = []
        self.objects = []
        return
    
    def reset_map(self):
        self.map = choose_random_map("maps.json")
        valid_x, valid_y = find_spawn_point(self.map, self.box_resolution)
        self.npc = NPC(valid_x,valid_y,5)
        self.objects = []
        self.objects.append(self.npc)
        self.walls = []
        self.gen_boundaries()
        self.draw_map()
        self.player.tagged = True
        self.npc.tagged = False
        self.score+=1
        return


    def enter(self):
        self.score = 0
        self.map = choose_random_map("maps.json")
        #self.map = choose_map("maps.json", "map_1")
        #self.map = get_last_map("maps.json")
        print(f"Entering: {self.name}")

        valid_x, valid_y = find_spawn_point(self.map, self.box_resolution)
        self.player = Player(valid_x, valid_y,5)
        
        valid_x, valid_y = find_spawn_point(self.map, self.box_resolution)
        self.npc = NPC(valid_x,valid_y,5)
        self.objects.append(self.npc)

        self.gen_boundaries()
        self.draw_map()
        self.player.tagged = True
        self.npc.tagged = False
        
        return
    
    def leave(self):
        print(f"Leaving: {self.name}")
        self.walls = []
        return
    
    def get_val_from_map(self,x,y):
        if((0 <= x and x <= len(self.map[0])-1) and (0 <= y and y <= len(self.map)-1)):
            return self.map[y][x]
        return None
    
    def gen_lines(self, x_offset, y_offset, x_check, y_check):
        res = self.box_resolution

        def create_vector(x, y, is_horizontal):
            if is_horizontal:
                return Vector(x * res, y * res + y_offset), Vector(x * res + res, y * res + y_offset)
            else:
                return Vector(x * res + x_offset, y * res), Vector(x * res + x_offset, y * res + res)

        def add_wall(start_vector, end_vector):
            self.walls.append(Boundary(start_vector, end_vector))

        for y in range(len(self.map)):
            start_vector = None

            for x in range(len(self.map[0])):
                val = self.get_val_from_map(x, y)

                if val != 0 and start_vector is None:
                    if self.get_val_from_map(x + x_check, y + y_check) == 0:
                        start_vector, end_vector = create_vector(x, y, is_horizontal=(y_check != 0))
                elif val != 0 and start_vector is not None:
                    if self.get_val_from_map(x + x_check, y + y_check) == 0:
                        end_vector = create_vector(x, y, is_horizontal=(y_check != 0))[1]
                    else:
                        add_wall(start_vector, end_vector)
                        start_vector = None
                elif val == 0 and start_vector is not None:
                    add_wall(start_vector, end_vector)
                    start_vector = None

            if start_vector is not None:
                add_wall(start_vector, end_vector)

    def gen_boundaries(self):
        self.gen_lines(self.box_resolution, 0, 1, 0)
        self.gen_lines(0, 0, -1, 0)
        self.gen_lines(0, self.box_resolution, 0, 1)
        self.gen_lines(0, 0, 0, -1)
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
        if(self.debug_mode):
            window.blit(self.map_img, (0,0))
        index_x = int(self.player.x/res)
        index_y = int(self.player.y/res)
        self.player.render(window,self.walls,self.objects)
        if(self.debug_mode):
            for wall in self.walls:
                wall.render(window)
            for obj in self.objects:
                obj.render(window)
        return

    def update(self):
        keys = pygame.key.get_pressed()
        self.mouseX,self.mouseY = pygame.mouse.get_pos()
        self.mouseB = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.debug_mode = not self.debug_mode
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
        self.player.update(keys,(self.mouseX,self.mouseY,self.mouseB),self.map,self.box_resolution,self.objects) 
        
        for obj in self.objects:
            d = math.sqrt(math.pow(obj.x-self.player.position[0],2) + math.pow(obj.y-self.player.position[1],2))
            if(d<self.player.radius+obj.radius):
                self.reset_map()  

        self.clock.tick(60)  
        return