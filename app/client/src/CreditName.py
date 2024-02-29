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

        #Random number for velocity for x and y, and the color of the rectangle
        self.velX, self.velY = randX,randY
        self.color = (randR,randG,randB)

    def create_name(self):
        #Returns a rectangle
        name = pygame.Rect(self.rectX,self.rectY,self.width,self.height)
        return name
        

    def bounce(self, state_machine):
        #Helps manages the credit name bouncing off the screen

        self.top = self.rectY +self.height
        self.bottom = self.rectY
        self.right = self.rectX +self.width
        self.left = self.rectX

        if (self.right >= state_machine.window_width) or (self.left <= 0):
            self.velX = -self.velX
        if (self.top >= state_machine.window_height) or (self.bottom <= 0):
            self.velY = -self.velY

    
    def move(self):
        #Moves the rectangle based on velocity
        self.rectX += self.velX
        self.rectY += self.velY

    def adjustment(self):
        
        self.top = self.rectY +self.height
        self.bottom = self.rectY
        self.right = self.rectX +self.width
        self.left = self.rectX


        
    


    
