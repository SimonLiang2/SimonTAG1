import pygame

class EndGameState:
    def __init__(self,name):
        self.name = name
        self.best_score = 0
        self.state_machine = None
        self.font_size = 50
    
    def enter(self):
        if(self.state_machine.player_score > self.best_score):
            self.best_score = self.state_machine.player_score
        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")
    
    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

        font = pygame.font.SysFont('Georgia',self.font_size)
        text = font.render(f"Your Score: {self.state_machine.player_score}", True, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = ((self.state_machine.window_width/2), 130) 
        window.blit(text, text_rect)

        text = font.render(f"Best Score: {self.best_score}", True, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = ((self.state_machine.window_width/2), 180) 
        window.blit(text, text_rect)

        text = font.render(f"Hit Space to Continue...", True, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = ((self.state_machine.window_width/2)+20, 260) 
        window.blit(text, text_rect)

        font = pygame.font.SysFont('Georgia',int(self.font_size/2))
        text = font.render(f"Dev Score: {40}", True, (255,255,255)) 
        text_rect = text.get_rect()
        text_rect.center = (140, 40) 
        window.blit(text, text_rect)
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_SPACE:
                    self.state_machine.transition("menu")