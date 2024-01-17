import USB_Device

L = "L"
R = "R"
ZL = "ZL"
ZR = "ZR"
LS = "LS"
RS = "RS"
A = "A"
B = "B"
X = "X"
Y = "Y"
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
PLUS = "+"
MINUS = "-"
HOME = "HOME"
SCREENSHOT = "SCREENSHOT"

def parse_input(input):
	output = []

	try:
		if input[0]&1:
			output.append(Y)
		if input[0]&2:
			output.append(B)
		if input[0]&4:
			output.append(A)
		if input[0]&8:
			output.append(X)
		if input[0]&16:
			output.append(ZL)
		if input[0]&32:
			output.append(ZR)
		if input[0]&64:
			output.append(L)
		if input[0]&128:
			output.append(R)
		if input[1]&1:
			output.append(MINUS)
		if input[1]&2:
			output.append(PLUS)
		if input[1]&4:
			output.append(LS)
		if input[1]&8:
			output.append(RS)
		if input[1]&16:
			output.append(HOME)
		if input[1]&32:
			output.append(SCREENSHOT)
			
		if input[2]==0:
			output.append(UP)
		elif input[2]==1:
			output.append(UP)
			output.append(RIGHT)
		elif input[2]==2:
			output.append(RIGHT)
		elif input[2]==3:
			output.append(RIGHT)
			output.append(DOWN)
		elif input[2]==4:
			output.append(DOWN)
		elif input[2]==5:
			output.append(DOWN)
			output.append(LEFT)
		elif input[2]==6:
			output.append(LEFT)
		elif input[2]==7:
			output.append(LEFT)
			output.append(UP)
			
	finally:
		return output
