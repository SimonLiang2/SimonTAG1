import pygame
from ClientSocket import ClientSocket

class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.window_should_close = False
        pygame.init()
        self.window_width = 1000
        self.window_height = 600
        self.player_score = 0
        self.client_socket = ClientSocket('127.0.0.1')
        self.client_socket.start_thread()
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Tag Game")
        return

    def add_state(self,state):
        if(state.name not in self.states):
            state.state_machine = self
            self.states[state.name] = state
        return
    
    def transition(self,name):
        if(name in self.states):
            if(self.current_state):
                self.current_state.leave()
            self.current_state = self.states[name]
            self.current_state.enter()
        return