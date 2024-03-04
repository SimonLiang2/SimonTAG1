import time as times
class GameTimer:
    def __init__(self, coords, end_func, color=(0,0,0), time=90):
        self.start_time = time+1
        self.epoch_time = int(times.time())
        self.time = time+1
        self.coords = coords
        self.color = color
        self.end_func = end_func
    
    def tick(self):
        if self.time > 0:
            self.time -= 1
        else:
            self.end_func()
    def update(self):
        if self.epoch_time < int(times.time()):
            self.tick()
            self.epoch_time = int(times.time())
            #print(self.time)
    def reset(self):
        self.time = self.start_time