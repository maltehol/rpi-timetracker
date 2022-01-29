from RPLCD.gpio import CharLCD as LCD
import RPi.GPIO as GPIO


class LCDWriter:

    # LCD
    rs = 17
    en = 27
    rw = 4
    d7 = 18
    d6 = 23
    d5 = 24
    d4 = 25

    def __init__(self):
        self.lcd = LCD(pin_rs=self.rs, pin_rw=self.rw, pin_e=self.en, pins_data=[
                       self.d4, self.d5, self.d6, self.d7], numbering_mode=GPIO.BCM, cols=16, rows=2, compat_mode=True)
        self.top_line = ''
        self.bottom_line = ''

    def writeTop(self, line):
        if self.top_line == line:
            return
        self.top_line = line
        self.refresh()

    def writeBottom(self, line):
        if self.bottom_line == line:
            return
        self.bottom_line = line
        self.refresh()

    def refresh(self):
        self.lcd.clear()
        self.lcd.cursor_pos = (0, 0)
        self.lcd.write_string(self.top_line)
        self.lcd.cursor_pos = (1, 0)
        self.lcd.write_string(self.bottom_line)

