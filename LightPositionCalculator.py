import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def calculate_track_length(a, b):
	x_diff = b.x - a.x
	y_diff = b.y - a.y
	return math.sqrt((x_diff**2) + (y_diff**2))


POINT_A = Point(1072, 70) # point at beginning of data line
POINT_B = Point(1229, 223) # point at end of data line
OFFSET = 242 # number of lights with positions already calculated (last light +1)

DISTANCE_BETWEEN_LIGHTS = (50/3) # center to center in millimeters

def arbitrary_round(x, prec=3, base=DISTANCE_BETWEEN_LIGHTS):
	return round(base * round(float(x)/base, prec))

TRACK_LENGTH = arbitrary_round(calculate_track_length(POINT_A, POINT_B))
LIGHTS_ON_TRACK = round(TRACK_LENGTH / DISTANCE_BETWEEN_LIGHTS) + 1
X_INCREMENT = (POINT_B.x - POINT_A.x) / (LIGHTS_ON_TRACK - 1)
Y_INCREMENT = (POINT_B.y - POINT_A.y) / (LIGHTS_ON_TRACK - 1)

for n in range(LIGHTS_ON_TRACK):
	x_pos = round(POINT_A.x + (n * X_INCREMENT))
	y_pos = round(POINT_A.y + (n * Y_INCREMENT))
	print(str(n + OFFSET) + " : c.Point(" + str(x_pos) + ", " + str(y_pos) + "),")

 # 1287
