
from lcdWriter import LCDWriter


class SimpleWriter:
    def __init__(self):
        self.lcd = LCDWriter()

    def writeState(self, state):
        if state.globalTaskTimer.isPaused():
            self.writeTask('Pause')
            self.writeTime(state.globalTaskTimer)
            return

        if state.currentTask is None:
            self.writeTask('<ohne Aufgabe>')
            self.writeTime(state.globalTaskTimer)
            return

        self.writeTask(state.currentTask.name)
        self.writeTime(state.globalTaskTimer, state.currentTask.timer)

        

    def writeLog(self, task):
        # In/Out , taskname , timestamp
        line = ''
        if task.isStopped:
            line += 'OUT,'
        else
            line +='IN,'

        line += f'{task.name},{task.timer.timestamps[-1]}\n'

        with open('time_traking.csv', 'a') as csv:
            csv.write(line)

    def writeTime(self, stopwatchRight, stopwatchLeft=None):

        right = str(stopwatchRight)
        left = '     '

        if stopwatchLeft is not None:
            left = str(stopwatchLeft)

        self.lcd.writeBottom(left + '      ' + right)

    def writeTask(self, string):
        self.lcd.writeTop(string)
