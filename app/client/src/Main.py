import pygame
from StateMachine import StateMachine
from GameState import GameState
from MessageState import MessageState
from MainMenu import MainMenu
from CreditsState import CreditsState
from SettingsState import SettingsState
from InfoState import InfoState
from VolumeState import VolumeState
from BindsState import BindsState
from HistoricalState import HistoricalState
import random as r

state_machine = StateMachine()
game_state = GameState("game")
menu_state = MainMenu("menu")
end_state = MessageState("message")
credits_state = CreditsState("credits")
settings_state = SettingsState("settings")
info_state = InfoState("info")
volume_state = VolumeState("volume")
historical_state = HistoricalState("historical")
binds_state = BindsState("binds")
state_machine.add_state(game_state)
state_machine.add_state(menu_state)
state_machine.add_state(credits_state)
state_machine.add_state(settings_state)
state_machine.add_state(info_state)
state_machine.add_state(end_state)
state_machine.add_state(volume_state)
state_machine.add_state(historical_state)
state_machine.add_state(binds_state)

state_machine.transition("menu")

while not state_machine.window_should_close:
    state_machine.current_state.update()
    state_machine.current_state.render(state_machine.window)
    pygame.display.flip()
if(state_machine.client_socket): state_machine.client_socket.send_data("kill-socket")
pygame.quit()