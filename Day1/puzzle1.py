f = open("input1.txt", 'r')
data = f.read()
position = 0
floor = 0
flag = True
for char in data:
	position += 1
	if char == ')':
		floor -= 1
		if floor < 0:
			if flag:
				print(position)
				flag = False
	if char == '(':
		floor += 1

print(floor)