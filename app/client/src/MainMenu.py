import pygame
import time
from MenuButton import MenuButton

class MainMenu:
    def __init__(self,name):
        self.name = name
        self.state_machine = None
        self.active_button_idx = 0
        self.buttons = []

        self.last_input_method = 'keyboard'
        self.last_mouse_pos = pygame.mouse.get_pos()

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
        button_scale = .45
        self.play_button = MenuButton("Play", self.play_pressed, image_path=play_filepath, scale=button_scale)
        self.credits_button = MenuButton("Credits",self.credits_pressed, image_path=credits_filepath, scale=button_scale)
        self.quit_button = MenuButton("Quit", self.quit_pressed, image_path=quit_filepath, scale=button_scale)

        # Keep track of all the buttons publicly using a list
        self.buttons = [self.play_button, self.credits_button, self.quit_button]

        logo_path = 'app/client/src/assets/images/logo.png'
        self.logo = self.create_image(logo_path, rescale=.5)

        self.settings_inverted_path = 'app/client/src/assets/images/settings-inverted.png'
        self.settings_path = 'app/client/src/assets/images/settings.png'
        self.settings = self.create_image(self.settings_path, rescale=.4)

        self.info_path = 'app/client/src/assets/images/infoicon.png'
        self.info_path_inverted = 'app/client/src/assets/images/infoicon-inverted.png'
        self.info = self.create_image(self.info_path, rescale=0.3)
    
    def enter(self):
        # Catch any exceptions when trying to load audio
        try:
            # Play music
            pygame.mixer.init()
            pygame.mixer.music.load(self.menu_music_filepath)
            pygame.mixer.music.set_volume(0.5 * self.state_machine.master_volume)
            pygame.mixer.music.play(loops=-1)
            

            self.button_selected_sound = pygame.mixer.Sound(self.button_select_filepath)
            self.button_selected_sound.set_volume(0.6 * self.state_machine.master_volume)

            self.enter_sound = pygame.mixer.Sound(self.enter_key_filepath)
            self.enter_sound.set_volume(1 * self.state_machine.master_volume)

            self.quit_sound = pygame.mixer.Sound(self.quit_sound_filepath)
            self.quit_sound.set_volume(1 * self.state_machine.master_volume)
        except FileNotFoundError as no_file_e:
            print(f"File Not Found Error: {no_file_e}")
        except Exception as exception:
            print(f"Exception caught: {exception}")
    
    def leave(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    # User has selected the play button
    def play_pressed(self):
        time.sleep(0.4)
        self.state_machine.transition("game")
        #pygame.mixer.music.stop()
        #print("PLAY PRESSED")

    # User has selected the credits button
    def credits_pressed(self):
        self.state_machine.transition("credits")
        #print("CREDITS PRESSED")

    # User has selected the quit button
    def quit_pressed(self):
        # Send signal to the state machine to close windows
        time.sleep(0.4)
        self.state_machine.window_should_close = True
        #print("QUIT PRESSED")

        # Creates and returns a title logo
    def create_image(self, image_path, rescale=1):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (image.get_width() * rescale, image.get_height() * rescale))
        return image

    def render(self,window=None):
        window.fill(self.window_color)        

        # Add the logo to the window
        window.blit(self.logo, (self.state_machine.window_width//2-162,self.state_machine.window_height//12))

        # Add settings  & info icon to window
        window.blit(self.settings, (20,525))
        window.blit(self.info, (90, 525))

        # Blit each button to the window
        # If the button is active(active_button_idx) then set active=True
        button_x,button_y =  self.state_machine.window_width//2-150,250
        for i,button in enumerate(self.buttons):
            if i == self.active_button_idx:
                window.blit(button.create_button(active=True), (button_x,button_y))
            else: 
                window.blit(button.create_button(), (button_x,button_y))
            button_y+=100 # So they all don't get placed on top of each other


    def update(self):
        current_mouse_pos = pygame.mouse.get_pos()

        # Hover over settings
        if (current_mouse_pos[0] >= 19 and current_mouse_pos[0] <= 78) and (current_mouse_pos[1] >= 525 and current_mouse_pos[0] <= 586):
            self.settings = self.create_image(self.settings_inverted_path, rescale=.07)
        else:
            self.settings = self.create_image(self.settings_path, rescale=.07)

        if (current_mouse_pos[0] >= 100 and current_mouse_pos[0] <= 147) and (current_mouse_pos[1] >= 533 and current_mouse_pos[0] <= 588):
            self.info = self.create_image(self.info_path_inverted, rescale=0.3)
        else:
            self.info = self.create_image(self.info_path, rescale=0.3)


        # Check if the mouse has moved since the last frame
        if self.last_mouse_pos != current_mouse_pos:
            self.last_input_method = 'mouse'
        self.last_mouse_pos = current_mouse_pos  # Update the last mouse position for the next frame

        # Update active button index based on mouse position only if the last input was from the mouse
        if self.last_input_method == 'mouse':
            if (current_mouse_pos[0] >= 367) and (current_mouse_pos[0] <= 651) and (current_mouse_pos[1] >= 257) and (current_mouse_pos[1] <= 334):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                self.active_button_idx = 0
            elif (current_mouse_pos[0] >= 367) and (current_mouse_pos[0] <= 651) and (current_mouse_pos[1] >= 362) and (current_mouse_pos[1] <= 432):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                self.active_button_idx = 1
            elif (current_mouse_pos[0] >= 367) and (current_mouse_pos[0] <= 651) and (current_mouse_pos[1] >= 462) and (current_mouse_pos[1] <= 529):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                self.active_button_idx = 2
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.window_should_close = True
            
            # Handle keyboard inputs
            elif event.type == pygame.KEYDOWN:
                self.last_input_method = 'keyboard'  # Update last input method to keyboard on key press
                key = event.key
                if key == pygame.K_UP:
                    self.button_selected_sound.play()
                    if self.active_button_idx > 0:
                        self.active_button_idx -= 1
                    else:
                        self.active_button_idx = len(self.buttons) - 1
                elif key == pygame.K_DOWN:
                    self.button_selected_sound.play()
                    if self.active_button_idx < len(self.buttons) - 1:
                        self.active_button_idx += 1
                    else:
                        self.active_button_idx = 0
                elif key == pygame.K_RETURN:
                    if self.active_button_idx == len(self.buttons) - 1:
                        self.quit_sound.play()
                    else:
                        self.enter_sound.play()
                    time.sleep(0.4)  # Give the sound time to finish
                    self.buttons[self.active_button_idx].pressed()
                elif key == pygame.K_ESCAPE:
                    self.quit_sound.play()
                    time.sleep(0.4)  # Give the sound time to finish
                    self.state_machine.window_should_close = True

            # Handle mouse button clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.last_input_method = 'mouse'  # Update last input method to mouse on click
                self.quit_sound.play()
                #time.sleep(0.5)  # Give the sound time to finish
                click_pos = pygame.mouse.get_pos()
                
                # Check if the click is within the bounds of the buttons and act accordingly
                if (click_pos[0] >= 367) and (click_pos[0] <= 651) and (click_pos[1] >= 257) and (click_pos[1] <= 334):
                    self.active_button_idx = 0
                    self.buttons[self.active_button_idx].pressed()
                elif (click_pos[0] >= 367) and (click_pos[0] <= 651) and (click_pos[1] >= 362) and (click_pos[1] <= 432):
                    self.active_button_idx = 1
                    self.buttons[self.active_button_idx].pressed()
                elif (click_pos[0] >= 367) and (click_pos[0] <= 651) and (click_pos[1] >= 462) and (click_pos[1] <= 529):
                    self.active_button_idx = 2
                    self.buttons[self.active_button_idx].pressed()
                elif (click_pos[0] >= 19 and click_pos[0] <= 78) and (click_pos[1] >= 525 and click_pos[0] <= 586):
                    #print("Settings Icon Clicked")
                    self.state_machine.transition("settings")
                elif (current_mouse_pos[0] >= 100 and current_mouse_pos[0] <= 147) and (current_mouse_pos[1] >= 533 and current_mouse_pos[0] <= 588):
                    #print("Info Icon Clicked")
                    self.state_machine.transition("info")
                #print(f"Mouseclick at: {click_pos}")