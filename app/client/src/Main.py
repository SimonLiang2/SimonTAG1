import pygame
from StateMachine import StateMachine
from GameState import GameState
from MainMenu import MainMenu
from CreditsState import CreditsState

state_machine = StateMachine()
game_state = GameState("game")
menu_state = MainMenu("menu")
credits_state = CreditsState("credits")
state_machine.add_state(game_state)
state_machine.add_state(menu_state)
state_machine.add_state(credits_state)

state_machine.transition("menu")

while not state_machine.window_should_close:
    state_machine.current_state.update()
    state_machine.current_state.render(state_machine.window)
    pygame.display.flip()
    pass
pygame.quit()