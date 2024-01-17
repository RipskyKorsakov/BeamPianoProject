import USB_Device

LB = "L"
RB = "R"
LS = "LS"
RS = "RS"
A = "A"
B = "B"
X = "X"
Y = "Y"
UP = "UP"
LEFT = "LEFT"
RIGHT = "RIGHT"
DOWN = "DOWN"
START = "START"
BACK = "SELECT"
DOWNLOAD = "DOWNLOAD"

def parse_input(input):
	output = []
	
	try:
		if input[5]&1:
			output.append(UP)
		if input[5]&2:
			output.append(DOWN)
		if input[5]&4:
			output.append(LEFT)
		if input[5]&8:
			output.append(RIGHT)
		if input[5]&16:
			output.append(LB)
		if input[5]&32:
			output.append(RB)
		if input[5]&64:
			output.append(LS)
		if input[5]&128:
			output.append(RS)
		if input[4]&4:
			output.append(START)
		if input[4]&8:
			output.append(BACK)
		if input[4]&16:
			output.append(A)
		if input[4]&32:
			output.append(B)
		if input[4]&64:
			output.append(X)
		if input[4]&128:
			output.append(Y)
		if input[18]&1:
			output.append(DOWNLOAD)
	finally:
		return output
	
