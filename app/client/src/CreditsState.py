import pygame
import random
from CreditName import CreditName


class CreditsState:
    
    def __init__(self,name):
        pygame.init()
        self.name = name
        self.state_machine = None

        # Create a clock object
        self.clock = pygame.time.Clock()
        self.fps = 30

        self.simonName = CreditName(10,10,190,50,'Simon Liang')
        self.johnnyName = CreditName(400,150,190,50, 'John Pertell')
        self.beckyName = CreditName(10,300,240,50, 'Becky Ostrander')
        self.noahName = CreditName(400,450,190,50, 'Noah Breedy')
    
    def enter(self):
        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")
    
    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

        self.clock.tick(self.fps)

        self.simonRect = self.simonName.create_name()
        self.johnnyRect = self.johnnyName.create_name()
        self.beckyRect = self.beckyName.create_name()
        self.noahRect = self.noahName.create_name()

        self.nameCollide()

        #Manages the movement of the credit names and draws the updated positions of the rectangle
        self.simonName.bounce(self.state_machine)
        pygame.draw.rect(window, (219,165,255), self.simonName.create_name())
        self.simonName.move()

        self.simonName.adjustment()

        self.johnnyName.bounce(self.state_machine)
        pygame.draw.rect(window, self.johnnyName.color, self.johnnyName.create_name())
        self.johnnyName.move()

        self.johnnyName.adjustment()

        self.beckyName.bounce(self.state_machine)
        pygame.draw.rect(window, self.beckyName.color, self.beckyName.create_name())
        self.beckyName.move()

        self.beckyName.adjustment()

        self.noahName.bounce(self.state_machine)
        pygame.draw.rect(window, self.noahName.color, self.noahName.create_name())
        self.noahName.move()

        self.noahName.adjustment()

        
        font = pygame.font.SysFont('Georgia',30) 
        smallfont = pygame.font.SysFont('Georgia',25)

        escText = font.render('Press ESC key to go back', True, (255,255,255))
        #creditText = font.render('Credits',True, (255,255,255))
        devText = font.render('Developers', True, (255,255,255))

        window.blit(escText,(20,560))
        #window.blit(creditText, (250,10))
        window.blit(devText,(self.state_machine.window_width/2 - 80,10))
        window.blit(self.simonName.text,(self.simonName.rectX + 10, self.simonName.rectY+5))
        window.blit(self.johnnyName.text,(self.johnnyName.rectX +10, self.johnnyName.rectY+5))
        window.blit(self.beckyName.text,(self.beckyName.rectX+10, self.beckyName.rectY+5))
        window.blit(self.noahName.text,(self.noahName.rectX+10, self.noahName.rectY+5))
    
    def nameCollide(self):

        self.simonName.adjustment()
        self.johnnyName.adjustment()
        self.beckyName.adjustment()
        self.noahName.adjustment()

        #If they collide, the rectangles will go the opposite direction

        if self.simonRect.colliderect(self.johnnyRect) or self.johnnyRect.colliderect(self.simonRect):
            
            self.simonName.velX, self.johnnyName.velX = -self.simonName.velX, -self.johnnyName.velX
            self.simonName.velY ,self.johnnyName.velY = -self.simonName.velY, -self.johnnyName.velY
            

        if self.simonRect.colliderect(self.noahRect) or self.noahRect.colliderect(self.simonRect):
            
            self.simonName.velX, self.simonName.velY = -self.simonName.velX, -self.simonName.velY
            self.noahName.velX, self.noahName.velY = -self.noahName.velX, -self.noahName.velY

        if self.simonRect.colliderect(self.beckyRect) or self.beckyRect.colliderect(self.simonRect):
            
            self.simonName.velX, self.simonName.velY = -self.simonName.velX, -self.simonName.velY
            self.beckyName.velX, self.beckyName.velY = -self.beckyName.velX, -self.beckyName.velY
            

        if self.johnnyRect.colliderect(self.beckyRect) or self.beckyRect.colliderect(self.johnnyRect):

            self.johnnyName.velX, self.johnnyName.velY = -self.johnnyName.velX, -self.johnnyName.velY
            self.beckyName.velX, self.beckyName.velY = -self.beckyName.velX, -self.beckyName.velY

        if self.johnnyRect.colliderect(self.noahRect) or self.noahRect.colliderect(self.johnnyRect):

            self.johnnyName.velX, self.johnnyName.velY = -self.johnnyName.velX, -self.johnnyName.velY
            self.noahName.velX, self.noahName.velY = -self.noahName.velX, -self.noahName.velY

        if self.beckyRect.colliderect(self.noahRect) or self.noahRect.colliderect(self.beckyRect):

            self.beckyName.velX, self.beckyName.velY = -self.beckyName.velX, -self.beckyName.velY
            self.noahName.velX, self.noahName.velY = -self.noahName.velX, -self.noahName.velY

        
            

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.state_machine.transition("menu")