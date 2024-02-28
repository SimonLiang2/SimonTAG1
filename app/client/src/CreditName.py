import random
import pygame

class CreditName:
    def __init__(self,x,y,width,height,text):
        pygame.init()
        self.rectX = x
        self.rectY = y
        self.height = height
        self.width = width

        font = pygame.font.SysFont('Georgia',30)
        self.text= font.render(text, True, (255,255,255))
        

        randX = random.random()/2 +3
        randY = random.random()/2 +3
        randR = random.random() * 255
        randG = random.random() * 255
        randB = random.random() * 255
        self.velX, self.velY = randX,randY
        self.color = (randR,randG,randB)

    def create_name(self):
        name = pygame.Rect(self.rectX,self.rectY,self.width,self.height)
        return name
        

    def bounce(self):
        self.top = self.rectY +self.height
        self.bottom = self.rectY
        self.right = self.rectX +self.width
        self.left = self.rectX

        if (self.right >= 600) or (self.left <= 0):
            self.velX = -self.velX
        if (self.top >= 600) or (self.bottom <= 0):
            self.velY = -self.velY

    
    def move(self):
        self.rectX += self.velX
        self.rectY += self.velY

    def adjustment(self):
        self.top = self.rectY +self.height
        self.bottom = self.rectY
        self.right = self.rectX +self.width
        self.left = self.rectX


        
    


    
