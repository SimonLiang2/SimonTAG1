class GameState:
    def __init__(self,name):
        self.name = name
        return
    
    def enter(self):
        print(f"Entering: {self.name}")
        return
    
    def leave(self):
        print(f"Leaving: {self.name}")
        return
    
    def render(self,window=None):
        pass

    def update(self):
        pass
