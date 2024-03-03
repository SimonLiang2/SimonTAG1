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
        text1 = font.render('This works like regular tag but with multiple people!',True,(255,255,255))
        text2 = font.render('This is you! You will only be able to see where your mouse clicks.',True,(255,255,255))
        text3 = font.render('Try to not get tagged! If you do, tag someone before the time runs out!',True,(255,255,255))
        text4 = font.render('Whoever is it by the end of timer will be vanquished',True,(255,255,255))
        text5 = font.render('Have fun! Try and be the last one remaining!',True,(255,255,255))
        escText = font.render('Press ESC key to go back', True, (255,255,255))
        pygame.draw.circle(window, (0,0,200), (self.state_machine.window_width/2,240),20,0)

        pygame.draw.circle(window, (255,255,0), (self.state_machine.window_width/2,340),20,0)

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