class PlayerData:
    def __init__(self,x,y,tagged,id):
        self.x = x
        self.y = y
        self.it = tagged
        self.id = id
    
    def update(self,x,y,tagged,id):
        self.x = x
        self.y = y
        self.it = tagged
        self.id = id