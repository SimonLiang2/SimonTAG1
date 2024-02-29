import pygame
from StateMachine import StateMachine
from GameState import GameState
from MainMenu import MainMenu
from CreditsState import CreditsState
from SettingsState import SettingsState
from InfoState import InfoState
import random as r

valid_seeds = "app\\client\\src\\assets\\valid_seeds"
lines = open(valid_seeds).readlines()
seed = r.choice(lines).strip()
r.seed(seed)
print("Seed:", seed)

state_machine = StateMachine()
game_state = GameState("game")
menu_state = MainMenu("menu")
credits_state = CreditsState("credits")
settings_state = SettingsState("settings")
info_state = InfoState("info")
state_machine.add_state(game_state)
state_machine.add_state(menu_state)
state_machine.add_state(credits_state)
state_machine.add_state(settings_state)
state_machine.add_state(info_state)

state_machine.transition("menu")

while not state_machine.window_should_close:
    state_machine.current_state.update()
    state_machine.current_state.render(state_machine.window)
    pygame.display.flip()
    pass
pygame.quit()