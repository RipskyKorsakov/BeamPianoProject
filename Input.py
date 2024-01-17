import Dictionaries as dicts

OFF = 0
ON = 1
STANDBY = 2
STANDBY_COUNTER = 5 # Change this value to change the amount of time before a key press can be registered again

class Input:
    def __init__(self, index):
        self.index = index
        self.state = OFF
        self.standby_counter = 0

    def activate(self):
        if self.state == OFF:
            self.state = ON
            #generate circle
            return
        if self.state == ON:
            self.state = STANDBY
            self.standby_counter = STANDBY_COUNTER
            return
        if self.state == STANDBY:
            self.standby_counter = STANDBY_COUNTER

    def iterate(self):
        if self.state == OFF:
            return
        if self.state == ON:
            self.state = STANDBY
            self.standby_counter = STANDBY_COUNTER
            return
        if self.standby_counter > 0:
            self.standby_counter -= 1
            return
        if self.standby_counter == 0:
            self.state = OFF
            return

    def is_active(self):
        return self.state == ON

    def get_index(self):
        return self.index
