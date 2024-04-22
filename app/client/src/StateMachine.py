import pygame


class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.window_should_close = False
        pygame.init()
        self.window_width = 1000
        self.window_height = 600
        self.player_score = 0
        self.server_time_end = -2
        self.client_socket = None
        self.msg = None
        self.ip_address = '127.0.0.1'
        self.port = 3000
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.master_volume = 0.50
        self.keys = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]
        self.game_stats = [0,0]
        pygame.display.set_caption("Tag Game")
        try:
            with open("app\\client\\src\\stats.txt", "r") as txt_file:
                    self.game_stats = txt_file.readlines()
            self.game_stats[0] = int(self.game_stats[0])  
            self.game_stats[1] = int(self.game_stats[1])   
        except:
            self.game_stats = [0,0]
        return

    def add_state(self,state):
        if(state.name not in self.states):
            state.state_machine = self
            self.states[state.name] = state
        return
    
    def transition(self,name,msg=None):
        if(name in self.states):
            if(self.current_state):
                self.current_state.leave()
            self.current_state = self.states[name]
            self.msg = msg
            self.current_state.enter()
        return