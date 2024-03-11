import time as times

class ServerTimer:
    def __init__(self, time=15, wait_time=-3):
        self.start_time = time
        self.epoch_time = int(times.time())
        self.time = time
        self.wait_time = wait_time

    def tick(self):
        if self.time > self.wait_times:
            self.time -= 1
        elif self.time <= -5:
            self.reset()

    def update(self):
        if self.epoch_time < int(times.time()):
            self.tick()
            self.epoch_time = int(times.time())
        return self.time

    def reset(self):
        self.time = self.start_time
