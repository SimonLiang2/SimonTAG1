import pygame

class InfoState:
    def __init__(self,name):
        pygame.init()
        self.name = name
        self.state_machine = None
    
    def enter(self):
        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")
    
    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)
        font = pygame.font.SysFont('Georgia',30)
        infotext = font.render ('How to Play', True, (255,255,255))
        text1 = font.render('The objective is to find the Hidden Player!',True,(255,255,255))
        text2 = font.render('This is you! You will only be able to see where your mouse is held down.',True,(255,255,255))
        text3 = font.render('Navigate the world and find the hidden player in Time!',True,(255,255,255))
        text4 = font.render('Find them as many times as you can before the clock runs out',True,(255,255,255))
        text5 = font.render('Have fun! Gain as many points as possible!',True,(255,255,255))
        escText = font.render('Press ESC key to go back', True, (255,255,255))
        pygame.draw.circle(window, (255,255,0), (self.state_machine.window_width/2,240),20,0)

        pygame.draw.circle(window, (255,255,255), (self.state_machine.window_width/2 + 140,100),20,0)

        window.blit(infotext, (self.state_machine.window_width/2 - 80,10))
        window.blit(text1, (20,80))
        window.blit(text2, (20,180))
        window.blit(text3, (20,280))
        window.blit(text4, (20,380))
        window.blit(text5, (20,480))
        window.blit(escText,(20,560))
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.state_machine.transition("menu")