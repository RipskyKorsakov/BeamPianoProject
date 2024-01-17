RIPPLE_SPEED = 4

class Ripple:
    def __init__(self, x):
        self.left = x
        self.right = x
    
    def iterate(self):
        self.left += RIPPLE_SPEED
        self.right -= RIPPLE_SPEED
