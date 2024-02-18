from StateMachine import StateMachine
from GameState import GameState


state_machine = StateMachine()
game_state = GameState("Reuben")
state_machine.add_state(game_state)

state_machine.transition("Reuben")

