def calculate_box(l, w, h):
	side1 = 2*l*w
	side2 = 2*w*h
	side3 = 2*h*l

	area_box = side1 + side2 + side3

	if side1 <= side2 and side1 <= side3:
		area_box += int(side1/2)
	elif side2 <= side1 and side2 <= side3:
		area_box += int(side2/2)
	else:
		area_box += int(side3/2)
	
	return area_box

def calculate_ribbon(l, w, h):
	cubic_feet = l*w*h
	side1 = l*w
	side2 = w*h
	side3 = h*l

	if side1 <= side2 and side1 <= side3:
		cubic_feet += 2*l + 2*w
	elif side2 <= side1 and side2 <= side3:
		cubic_feet += 2*w + 2*h
	else:
		cubic_feet += 2*h + 2*l

	return cubic_feet

f = open("input.txt", 'r')
data = f.read()
data = data.split("\n")
totalSquareFeetWrappingPaper = 0
totalSquareFeetRibbon = 0
for row in data:
	dimensions = row.split("x")
	if len(dimensions) > 2:
		l = int(dimensions[0])
		w = int(dimensions[1])
		h = int(dimensions[2])
		totalSquareFeetWrappingPaper += calculate_box(l, w, h)
		totalSquareFeetRibbon += calculate_ribbon(l, w, h)

print("box:", totalSquareFeetWrappingPaper)
print("ribbon:", totalSquareFeetRibbon)