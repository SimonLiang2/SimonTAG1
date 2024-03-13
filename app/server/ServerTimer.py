import time as times
import random

class ServerTimer:
    def __init__(self, time=45, wait_time=-3):
        self.start_time = time
        self.epoch_time = int(times.time())
        self.time = time
        self.wait_time = wait_time
        self.map = self.choose_map()
    
    def choose_map(self, maxnum=110):
        num = random.randint(1,maxnum)
        return (f"map_{str(num)}")

    def tick(self):
        if self.time >= self.wait_time:
            self.time -= 1
            if self.time == 0: print(">> TIME IS UP!")
        elif self.time < self.wait_time:
            self.map = self.choose_map()
            print(f">> Round begins at {self.map}")
            self.reset()

    def update(self):
        if self.epoch_time < int(times.time()):
            self.tick()
            self.epoch_time = int(times.time())
            
        return self.time

    def reset(self):
        self.time = self.start_time
