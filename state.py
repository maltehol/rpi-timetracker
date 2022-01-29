
from stopwatch import StopWatch

class State:

    def __init__(self):
        self.currentTask = None
        self.globalTaskTimer = StopWatch()
        self.tasks = []

    def startTask(self, taskName):
        if self.currentTask is not None:
            self.currentTask.end()

        newTask = Task(taskName)
        self.currentTask = newTask
        self.tasks.append(newTask)

    def endCurrentTask(self):
        if self.currentTask is None:
            return

        self.currentTask.end()
        self.currentTask = None

    def toggleTask(self, taskName):
        if self.currentTask is not None and self.currentTask.name == taskName:
            self.endCurrentTask()
            return
        
        self.startTask(taskName)

    def pause(self):
        self.endCurrentTask()
        self.globalTaskTimer.pause()

    def resume(self):
        self.globalTaskTimer.resume()

    def toggle(self):
        if self.globalTaskTimer.isPaused():
            self.resume()
        else:
            self.pause()



class Task:

    def __init__(self, name):
        self.name = name
        self.timer = StopWatch()

    def end(self):
        self.timer.stop()

    def isEnded(self):
        self.timer.isStopped()

    def pause(self):
        self.timer.pause()

    def resume(self):
        self.timer.resume()
        