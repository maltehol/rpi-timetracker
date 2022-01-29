from state import State


class ButtonProcessor:

    # Inputs
    btn1 = 20
    btn2 = 26
    btn3 = 13
    btn4 = 16
    btn5 = 19
    btn6 = 12
    btn7 = 6

    def __init__(self):
        self.state = None

    def buttonName(self, pin):
        if(pin == self.btn2):
            return "Aufagabe 2"
        if(pin == self.btn3):
            return "Aufagabe 3"
        if(pin == self.btn4):
            return "Aufagabe 4"
        if(pin == self.btn5):
            return "Aufagabe 5"
        if(pin == self.btn6):
            return "Aufagabe 6"
        if(pin == self.btn7):
            return "Aufagabe 7"

    def button1Pressed(self, pin):
        if self.state is None:
            self.state = State()
            return

        self.state.toggle()

    def buttonPressed(self, pin):
        self.state.toggleTask(self.buttonName(pin))
