import pygame
import time
from MenuButton import MenuButton

class MainMenu:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        self.active_button_idx = 0
        self.buttons = []

        # Background color
        self.window_color = (0, 0, 0)

        # Audio filepaths
        self.menu_music_filepath = 'app/client/src/assets/music/menu.mp3'
        self.button_select_filepath = 'app/client/src/assets/music/button-select.mp3'
        self.enter_key_filepath = 'app/client/src/assets/music/enter-key.mp3'
        self.quit_sound_filepath = 'app/client/src/assets/music/quit.mp3'

        # Button filepaths
        play_filepath = 'app/client/src/assets/images/play.png'
        credits_filepath = 'app/client/src/assets/images/credits.png'
        quit_filepath = 'app/client/src/assets/images/quit.png'

        # Instantiate buttons
        button_scale = .35
        self.play_button = MenuButton("Play", self.play_pressed, image_path=play_filepath, scale=button_scale)
        self.credits_button = MenuButton("Credits",self.credits_pressed, image_path=credits_filepath, scale=button_scale)
        self.quit_button = MenuButton("Quit", self.quit_pressed, image_path=quit_filepath, scale=button_scale)

        # Keep track of all the buttons publicly using a list
        self.buttons = [self.play_button, self.credits_button, self.quit_button]

        logo_path = 'app/client/src/assets/images/logo.png'
        self.logo = self.create_logo(logo_path, rescale=.4)
    
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

            self.quit_sound = pygame.mixer.Sound(self.quit_sound_filepath)
            self.quit_sound.set_volume(1)
        except FileNotFoundError as no_file_e:
            print(f"File Not Found Error: {no_file_e}")
        except Exception as exception:
            print(f"Exception caught: {exception}")

        print(f"Entering: {self.name}")
    
    def leave(self):
        print(f"Leaving: {self.name}")
    
    # User has selected the play button
    def play_pressed(self):
        self.state_machine.transition("game")
        pygame.mixer.stop()
        print("PLAY PRESSED")

    # User has selected the credits button
    def credits_pressed(self):
        self.state_machine.transition("credits")
        print("CREDITS PRESSED")
    
    # User has selected the quit button
    def quit_pressed(self):
        # Send signal to the state machine to close window
        self.state_machine.window_should_close = True
        print("QUIT PRESSED")

    def render(self,window=None):
        window.fill(self.window_color)

        # Add the logo to the window
        window.blit(self.logo, (157,50))
        
        # Blit each button to the window
        # If the button is active(active_button_idx) then set active=True
        button_x,button_y = 175,250
        for i,button in enumerate(self.buttons):
            if i == self.active_button_idx:
                window.blit(button.create_button(active=True), (button_x,button_y))
            else: 
                window.blit(button.create_button(), (button_x,button_y))
            button_y+=75 # So they all don't get placed on top of each other

    # Creates and returns a title logo
    def create_logo(self, image_path, rescale=1):
        logo = pygame.image.load(image_path)
        logo = pygame.transform.scale(logo, (logo.get_width() * rescale, logo.get_height() * rescale))
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
                    if self.active_button_idx < len(self.buttons) - 1:
                        self.enter_sound.play()
                    else:
                        self.quit_sound.play()
                    time.sleep(0.4) # give the enter_sound time to finish
                    self.buttons[self.active_button_idx].pressed()
                elif key == pygame.K_ESCAPE:
                    self.quit_sound.play()
                    time.sleep(0.4) # give the enter_sound time to finish
                    self.state_machine.window_should_close = True