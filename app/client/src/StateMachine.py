class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None
        return

    def add_state(self,state):
        if(state.name not in self.states):
            self.states[state.name] = state
        return
    
    def transition(self,name):
        if(name in self.states):
            if(self.current_state):
                self.current_state.leave()
            self.current_state = self.states[name]
            self.current_state.enter()
        return