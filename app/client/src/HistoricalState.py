import pygame

class HistoricalState:
    def __init__(self,name,color=(0,0,0)):
        self.name = name
        self.state_machine = None
        self.color = color
        self.font_size_button = 45
        self.font_size_title = 70
        self.games_won = 0
        self.games_played = 0
    
    def enter(self):
        self.games_won = self.state_machine.game_stats[0]
        self.games_played = self.state_machine.game_stats[1]

    
    def leave(self):
        pass

    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

        #Title
        font = pygame.font.SysFont('Georgia',self.font_size_title)
        text = font.render("HISTORICAL STATS", True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, self.state_machine.window_height//6) 
        window.blit(text, text_rect)

        #Games Won Text
        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render((f"Games Won: {round(self.games_won)}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 250) 
        window.blit(text, text_rect)

        #Games Played Text
        font = pygame.font.SysFont('Georgia',self.font_size_button)
        text = font.render((f"Games Played: {round(self.games_played)}"), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (self.state_machine.window_width/2, 325) 
        window.blit(text, text_rect)

        #ESC Text
        font = pygame.font.SysFont('Georgia',30)
        text = font.render(("Press ESC to go back."), True, self.color, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (150,570)
        window.blit(text, text_rect)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #X button is hit
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN: #If a key is hit. Only handles ESC
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.state_machine.transition("settings")