import pygame
import time
from MenuButton import MenuButton

class MainMenu:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        self.active_button_idx = 0
        self.buttons = []

        self.menu_music_filepath = 'app/client/src/music/menu.mp3'
        self.button_select_filepath = 'app/client/src/music/button-select.mp3'
        self.enter_key_filepath = 'app/client/src/music/entr-key.mp3'
    
    def enter(self):

        # Catch any exceptions when trying to load audio
        try:
            # Play music
            pygame.mixer.init()
            pygame.mixer.music.load(self.menu_music_filepath)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(loops=-1)

            self.button_selected_sound = pygame.mixer.Sound(self.button_select_filepath)
            self.button_selected_sound.set_volume(0.6)

            self.enter_sound = pygame.mixer.Sound(self.enter_key_filepath)
            self.enter_sound.set_volume(1)
        except FileNotFoundError as no_file_e:
            print(f"File Not Found Error: {no_file_e}")
        except Exception as exception:
            print(f"Exception caught: {exception}")

        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")
    
    # User has selected the play button
    def play_pressed(self):
        pygame.mixer.stop()
        self.state_machine.transition("game")
        print("PLAY GAME")

    # User has selected the credits button
    def credits_pressed(self):
        self.state_machine.transition("credits")
        print("CREDITS")
    
    # User has selected the quit button
    def quit_pressed(self):
        # Send signal to state machine to close window
        self.state_machine.window_should_close = True
        print("QUIT GAME")


    def render(self,window=None):
        color = (0, 0, 0)
        window.fill(color)

        # Add the logo to the window
        window.blit(self.create_logo("TAG"), (200,50))
        
        # Add each button to the window
        play_button = MenuButton("Play", "", self.play_pressed)
        credits_button = MenuButton("Credits", "", self.credits_pressed)
        quit_button = MenuButton("Quit", "", self.quit_pressed)

        # Keep track of all the buttons publicly using a list
        self.buttons = [play_button, credits_button, quit_button]

        # Draw each button to the window
        # If the button is active(active_button_idx) then set active=True
        button_x,button_y = 200,200
        for i,button in enumerate(self.buttons):
            if i == self.active_button_idx:
                window.blit(button.create_button(active=True), (button_x,button_y))
            else: 
                window.blit(button.create_button(), (button_x,button_y))
            button_y+=50 # Just so they all don't place on top of each other

    # Creates and returns a title logo
    def create_logo(self, text):
        font = pygame.font.SysFont("Arial", 32)

        logo = font.render(text, True, (255, 0, 0))
        return logo

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            
            # Handle key events
            # Up & Down keys change the active button index
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_UP:
                    self.button_selected_sound.play()
                    if self.active_button_idx > 0:
                        self.active_button_idx -= 1
                    else:
                        self.active_button_idx = len(self.buttons) -1
                elif key == pygame.K_DOWN:
                    self.button_selected_sound.play()
                    if len(self.buttons) - 1 > self.active_button_idx:
                        self.active_button_idx += 1
                    else:
                        self.active_button_idx = 0
                # On enter key pressed -> press the active button
                elif key == pygame.K_RETURN:
                    self.enter_sound.play()
                    time.sleep(0.1) # give the enter_sound time to finish
                    self.buttons[self.active_button_idx].pressed()
                elif key == pygame.K_ESCAPE:
                    self.state_machine.window_should_close = True