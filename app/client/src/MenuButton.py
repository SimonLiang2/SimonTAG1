import pygame

class MenuButton:
    def __init__(self, name, pressed_func, image_path=None, scale=1):
        self.name = name
        self.image_path = image_path
        self.pressed_func = pressed_func
        self.scale = scale

    def pressed(self):
        print(f"{self.name} has been pressed")
        self.pressed_func()

    def create_button(self, active=False):
        if self.image_path is None:
            font = pygame.font.SysFont("Arial", 32)
            if active:
                logo = font.render(self.name, True, (255, 255, 255))
            else:
                logo = font.render(self.name, True, (255, 0, 0))
            return logo
        else:
            if active:
                inverted_path = self.image_path[0:(len(self.image_path)-4)]
                inverted_path += "-inverted.png"
                image = pygame.image.load(inverted_path)
                image = pygame.transform.scale(image, (image.get_width() * self.scale, image.get_height() * self.scale))
                return image
            else:
                image = pygame.image.load(self.image_path)
                image = pygame.transform.scale(image, (image.get_width() * self.scale, image.get_height() * self.scale))
                return image