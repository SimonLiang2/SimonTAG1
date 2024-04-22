import pygame
import time
import random as r
import math 
from Player import Player
from NPC import NPC
from FlashLightUtils import Boundary,Vector,Circle
from MapStates import gen_map, find_spawn_point;
from CreateMaps import choose_random_map, choose_map, get_last_map
from GameTimer import GameTimer
from ClientSocket import ClientSocket
import os

SLEEPTIME = 0.1
class GameState:
    def __init__(self,name):
        self.bg_music_path = 'assets/music/gamemusic.mp3'
        self.flashlight_sound_path = 'assets/music/flashlight.mp3'
        self.game_timer = None
        self.name = name
        self.state_machine = None
        self.player = None
        self.map = None
        self.map_img = None
        self.box_resolution = 50
        self.mouseX = 0
        self.mouseY = 0
        self.mouseB = -1
        self.saved_tag = False
        self.reset_once = False
        self.check_it_once = False
        self.clock = pygame.time.Clock()
        self.debug_mode = False
        self.walls = []
        self.objects = []
        self.round_started = False
        self.tagged_player = None
        
    
    def check_it(self):
        if(not self.check_it_once and self.state_machine.client_socket.admin):
            self.check_it_once = True
            self.state_machine.client_socket.send_data("get-new-tagger")

    def reset_map(self):
        if(not self.reset_once):
            self.state_machine.client_socket.send_data("map-req")
            time.sleep(SLEEPTIME)    
            self.map = choose_map("maps.json",self.state_machine.client_socket.map_name)

            valid_x, valid_y = find_spawn_point(self.map, self.box_resolution)
            if self.player.tagged:
                self.player = Player(valid_x,valid_y,5)
                self.player.tagged = True
                #comment this out if you want the tagger to keep playing
                self.state_machine.transition("message","You Lose")
            else:
                self.player = Player(valid_x, valid_y,5)
                print ("You Survived...")
            self.tagged_player = None

            self.objects = []
            self.walls = []
            self.gen_boundaries()
            self.draw_map()
            self.players_in_game = 0
            self.reset_once = True


    def enter(self):
        self.walls = []
        self.objects = []
        self.state_machine.client_socket = ClientSocket(self.state_machine.ip_address, self.state_machine.port)
        if(self.state_machine.client_socket.inited):
            self.state_machine.client_socket.start_thread()
        else:
            self.state_machine.transition("message","Failed To Connect to Server")

        self.state_machine.player_score = 0

        self.game_timer = GameTimer((100,200),color=(255,255,255))
        
        self.state_machine.client_socket.send_data("map-req")
        time.sleep(SLEEPTIME)    

        self.map = choose_map("maps.json",self.state_machine.client_socket.map_name)

        valid_x, valid_y = find_spawn_point(self.map, self.box_resolution)
        self.player = Player(valid_x, valid_y,5)
        
        valid_x, valid_y = find_spawn_point(self.map, self.box_resolution)
        self.gen_boundaries()
        self.draw_map()

        try:
            pygame.mixer.music.load(self.bg_music_path)
            pygame.mixer.music.set_volume(0.3 * self.state_machine.master_volume)
            pygame.mixer.music.play(loops=-1)

            self.flashlight_sound = pygame.mixer.Sound(self.flashlight_sound_path)
        except Exception as e:
            print(f"FILE EXCEPTION:{e}")
    
    def leave(self):
        if(self.round_started):
            self.state_machine.game_stats[1] = self.state_machine.game_stats[1] + 1

        f = open("stats.txt","w")
        f.write(f"{self.state_machine.game_stats[0]}\n{self.state_machine.game_stats[1]}")
        f.close()
        # make sure this socket dies
        if(self.state_machine.client_socket.admin):
            self.state_machine.client_socket.send_data("get-admin")
            time.sleep(SLEEPTIME)    

        self.state_machine.client_socket.send_data("kill-socket")
        time.sleep(SLEEPTIME)  

        self.walls = []
        self.objects = []
        pygame.mixer.stop()
    
    def get_val_from_map(self,x,y):
        x = int(x)
        y = int(y)
        if((0 <= x and x <= len(self.map[0])-1) and (0 <= y and y <= len(self.map)-1)):
            return self.map[y][x]
    
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
           
    def draw_map(self):
        res  = self.box_resolution
        self.map_img = pygame.Surface((self.state_machine.window_width, self.state_machine.window_height))
        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[0])):
                 col = (0,0,0)
                 if(self.map[i][j] == 1):
                     col = (255,255,255)
                 self.map_img.fill(col,(j*res,i*res,res,res)) 

    def render(self,window=None):
        background_color = (0, 0, 0)
        window.fill(background_color)
        text_msg = "Waiting To Start Match."
        text_col = (255,255,255)

        if(self.state_machine.client_socket.admin):
            text_msg = "Hit P to Start Match..."
        if(self.debug_mode):
            text_col = (0,0,0)
            window.blit(self.map_img, (0,0))

        if(not self.round_started):
                font = pygame.font.SysFont('Georgia',30)
                text = font.render(text_msg, True, text_col) 
                text_rect = text.get_rect()
                text_rect.center = (160, 30) 
                window.blit(text, text_rect)

        self.game_timer.render(window,self.debug_mode,self.state_machine.window_width)
                       
        self.player.render(window,self.walls,self.objects)
        if(self.debug_mode):
            for wall in self.walls:
                wall.render(window)
            for obj in self.objects:
                obj.render(window)

    def update(self):
        if(self.state_machine.client_socket.it_flag):
            self.player.tagged = True
            self.state_machine.client_socket.it_flag = False

        if(self.state_machine.client_socket.un_it_flag):
            valid_x, valid_y = find_spawn_point(self.map, self.box_resolution,3)
            self.player = Player(valid_x, valid_y,5)             
            self.player.tagged = False
            self.state_machine.client_socket.un_it_flag = False

        #dont ask...
        self.round_started = self.state_machine.client_socket.round_started
        self.state_machine.client_socket.round_started

        #Prevent from Joining on lobby full
        if(self.state_machine.client_socket.lobby_full):
            self.state_machine.transition("message","Lobby Full or Round Started")

        self.objects = []
        self.game_timer.time = 10

        self.game_timer.update(self.state_machine.client_socket.round_timer) 

        if(self.game_timer.time > 0):
            self.reset_once = False
            self.check_it_once = False
            keys = pygame.key.get_pressed()
            self.mouseX,self.mouseY = pygame.mouse.get_pos()
            self.mouseB = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.debug_mode = not self.debug_mode
                    if event.key == pygame.K_ESCAPE:
                        if(self.round_started):
                            self.state_machine.transition("message","You Lose")
                        else:
                            self.state_machine.transition("message","Leaving Lobby")
                    if event.key == pygame.K_p:
                        if(self.players_in_game > 1):
                            if(self.state_machine.client_socket.admin and not self.round_started):
                                self.round_started = True
                                for i in range(2):
                                    self.state_machine.client_socket.send_data("start-round")
                                    time.sleep(SLEEPTIME)

                if event.type == pygame.QUIT:
                    self.state_machine.window_should_close = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        self.flashlight_sound.play()
                    except Exception as e:
                        print(f"Can not play flashlight sound: {e}")

            pdata = self.state_machine.client_socket.player_data
            col = (255,255,255)
            if(pdata):
                self.players_in_game = len(pdata.items())
                if(self.players_in_game == 1 and self.round_started):
                    self.state_machine.game_stats[0] = self.state_machine.game_stats[0] + 1
                    self.state_machine.transition("message","YOU WIN YOURE AWESOME")
                for key,data in pdata.items():
                    if(key != self.state_machine.client_socket.id):
                        if(data[2]): 
                            self.tagged_player = [data[0],data[1],5]
                            col = (255,0,0)
                        self.objects.append(NPC(data[0],data[1],5,col))
                        col = (255,255,255)

            if(self.round_started):
                if(self.tagged_player != None):
                    d = math.sqrt(abs(math.pow(self.tagged_player[0]-self.player.x,2)) + abs(math.pow(self.tagged_player[1]-self.player.y,2)))
                    if(d<self.player.radius+self.tagged_player[2]):
                        self.player.tagged = True
                        self.tagged_player = None
                    
                    # get distace betwee tagged player and client player
                    # if distance is less than the both radius client player.tagged = true
                else:
                    if self.player.tagged:
                        for player in self.objects:
                            d = math.sqrt(abs(math.pow(player.x-self.player.position[0],2)) + abs(math.pow(player.y-self.player.position[1],2)))
                            if(d<self.player.radius+player.radius):
                                self.player.tagged = False
                                valid_x, valid_y = find_spawn_point(self.map, self.box_resolution,3)
                                self.player = Player(valid_x, valid_y,5)
                        
                        # get distace between tagged player and client player
                        # if distance is less than the both radius client player.tagged = false
            keys = [keys[self.state_machine.keys[0]],keys[self.state_machine.keys[1]],keys[self.state_machine.keys[2]],keys[self.state_machine.keys[3]]]
            self.player.update(keys,(self.mouseX,self.mouseY,self.mouseB),self.map,self.box_resolution,self.objects) 
            self.state_machine.client_socket.send_data("player-tick",[self.player.x,self.player.y,self.player.tagged])
        
        elif(self.game_timer.time <= self.state_machine.server_time_end):
            self.reset_map()
            time.sleep(SLEEPTIME * 2)
            self.check_it()
       
        
        self.clock.tick(60)  