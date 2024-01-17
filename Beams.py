BEAM_WIDTH = 50
BEAM_SPEED = 50

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Beam:
	def __init__(self, x):
		self.x = x
	
	def get_left_edge(self):
		return self.x + (BEAM_WIDTH / 2)
		
	def get_right_edge(self):
		return self.x - (BEAM_WIDTH / 2)
		
class LeftBeam(Beam):
	def iterate(self):
		self.x += BEAM_SPEED

class RightBeam(Beam):
	def iterate(self):
		self.x -= BEAM_SPEED
		
def point_is_in_beam(p, b):
	return p.x < b.get_left_edge() and p.x > b.get_right_edge()	
	
