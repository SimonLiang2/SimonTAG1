import time as times
import pygame
class GameTimer:
    def __init__(self, coords, color=(0,0,0), time=90):
        self.start_time = time
        self.epoch_time = int(times.time())
        self.time = time
        self.coords = coords
        self.color = color
        self.font_size = 30

    def render(self,window,debug,window_width):
        t = 0
        
        self.color = (255,255,255)
        if(debug):
            self.color = (0,0,0)

        if(self.time >= 0):
            t = self.time

        font = pygame.font.SysFont('Georgia',self.font_size)
        text = font.render(f"Round-Timer: {t}", True, self.color) 
        text_rect = text.get_rect()
        text_rect.center = ((window_width/2)-20, 30) 
        window.blit(text, text_rect)

        return
        
    def update(self,num):
        self.time = num

    def reset(self):
        self.time = self.start_time