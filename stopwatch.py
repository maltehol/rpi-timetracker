import time

class StopWatch:

    def __init__(self):
        self.timestamps = [time.time()]
        self.isStopped = False

    def secounds_lapsed(self):
        current_time = time.time()
        elapsed = 0
        lastTime = None
        for timestamp in self.timestamps:
            if lastTime is None:
                lastTime = timestamp
                continue

            elapsed += (timestamp - lastTime)
            lastTime = None

        if lastTime is not None:
            elapsed += (current_time - lastTime)

        return elapsed

    def pause(self):
        if self.isPaused() or self.isStopped:
            return
        
        self.toggle()

    def toggle(self):
        self.timestamps.append(time.time())

    def resume(self):
        if self.isStopped:
            return

        if self.isPaused():
            self.toggle()

    def stop(self):
        self.toggle()
        self.isStopped = True

    def isPaused(self):
        return len(self.timestamps) % 2 == 0

    def __str__(self):
        secounds = self.secounds_lapsed()
        minutes = (secounds / 100) % 60
        hours = (secounds / 100) / 60
        return time.strftime(f'{hours:02.0f}:{minutes:02.0f}')
