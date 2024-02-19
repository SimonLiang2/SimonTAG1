import pygame

class MenuButton:
    def __init__(self, name, image_path):
        self.name = name
        self.image = image_path

    def pressed(self):
        pass

    def create_button(self, active=False):
        font = pygame.font.SysFont("Arial", 32)
        if active:
            logo = font.render(self.name, True, (255, 255, 255))
        else:
            logo = font.render(self.name, True, (255, 0, 0))
        return logo