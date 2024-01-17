import sys
sys.path.append("./usr/local/lib/python3.9/dist-packages")
import usb.core
import board
import neopixel

ON = True
OFF = False

class Light:
    def __init__(self, index, pixels, position=0):
        self.index = index
        self.position = position
        self.pixels = pixels
        self.state = OFF


    def get_position(self):
        return self.position


    def turn_on(self, color):
        self.state = ON
        self.pixels[self.index] = color


    def turn_off(self):
        self.state = OFF
        self.pixels[self.index] = (0, 0, 0)

    def toggle(self, color):
        if self.state == ON:
            self.turn_off()
        else:
            self.turn_on(color)
        
    def change_color(self, color):
        if self.state == ON:
            self.turn_on(color)
            
    def is_on(self):
        return self.state