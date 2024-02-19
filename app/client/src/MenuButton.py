import pygame

class MenuButton:
    def __init__(self, name, image_path, pressed_func):
        self.name = name
        self.image = image_path
        self.pressed_func = pressed_func

    def pressed(self):
        print(f"{self.name} has been pressed")
        self.pressed_func()

    def create_button(self, active=False):
        font = pygame.font.SysFont("Arial", 32)
        if active:
            logo = font.render(self.name, True, (255, 255, 255))
        else:
            logo = font.render(self.name, True, (255, 0, 0))
        return logo