class color_cycler:
    def __init__(self):
        self.r = 255
        self.g = 0
        self.b = 0


    def get_color(self):
        return (self.r, self.g, self.b)

    def shift_color(self):
        if self.b == 0 and self.r > 0:
            self.shift_to_green()
            return
        if self.r == 0 and self.g > 0:
            self.shift_to_blue()
            return
        self.shift_to_red()

    def shift_to_red(self):
        self.b -= 1
        self.r += 1

    def shift_to_green(self):
        self.r -= 1
        self.g += 1

    def shift_to_blue(self):
        self.g -= 1
        self.b += 1
