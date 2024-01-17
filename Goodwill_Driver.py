import USB_Device

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
L1 = "L1"
L2 = "L2"
R1 = "R1"
R2 = "R2"
X = "X"
B = "B"
Y = "Y"
A = "A"
START = "START"
SELECT = "SELECT"

def parse_input(input):
	try:
		output = []

		if input[1] < 127:
			output.append(UP)
		elif(input[1] > 127):
			output.append(DOWN)
		    
		if (input[0] < 127):
			output.append(LEFT)
		elif (input[0] > 127):
			output.append(RIGHT)
		    
		i = input[2]
		if (i & 128):
			output.append(R2)
		if (i & 64):
			output.append(L2)
		if (i & 32):
			output.append(R1)
		if (i & 16):
			output.append(L1)
		if (i & 8):
			output.append(Y)
		if (i & 4):
			output.append(B)
		if (i & 2):
			output.append(A)
		if (i & 1):
			output.append(X)
		    
		j = input[3]
		if (j & 2):
		    output.append(START)
		if (j & 1):
            		output.append(SELECT)
	finally:
		return output
