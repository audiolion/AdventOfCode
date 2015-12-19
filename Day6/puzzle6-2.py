def print_matrix(m):
  for i in range(0, len(m)):
    print(m[i])

data = open("input.txt", 'r').read()
data = data.split("\n")
data = data[0:(len(data)-1)]

m = [[0] * 1000 for i in range(1000)]

TURN_ON = "turn on"
TURN_OFF = "turn off"
TOGGLE = "toggle"

for instruction in data:
	coords = instruction.split(" through ")
	secondPair = coords[1]
	secondPair = secondPair.split(",")
	if TURN_ON in instruction:
		firstPair = coords[0].split("on ")
		firstPair = firstPair[1].split(",")
		for i in range(int(firstPair[0]), int(secondPair[0])+1):
			for j in range(int(firstPair[1]), int(secondPair[1])+1):
				m[i][j] += 1
	elif TURN_OFF in instruction:
		firstPair = coords[0].split("off ")
		firstPair = firstPair[1].split(",")
		for i in range(int(firstPair[0]), int(secondPair[0])+1):
			for j in range(int(firstPair[1]), int(secondPair[1])+1):
				if m[i][j] > 0:
					m[i][j] -= 1
	elif TOGGLE in instruction:
		firstPair = coords[0].split("ggle ")
		firstPair = firstPair[1].split(",")
		for i in range(int(firstPair[0]), int(secondPair[0])+1):
			for j in range(int(firstPair[1]), int(secondPair[1])+1):
				m[i][j] += 2

lightsOn = 0
for i in range(0, len(m)):
	for j in range(0, len(m[i])):
		lightsOn += m[i][j]
print(lightsOn)