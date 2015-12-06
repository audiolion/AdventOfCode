f = open("input.txt", 'r')
data = f.read()

rowRobo = 0
colRobo = 0

rowSanta = 0
colSanta = 0
santa_grid = {"0,0": 1}
robo_grid = {}

turnSanta = True

for char in data:
	if char == '>':
		if turnSanta:
			rowSanta += 1
			position = str(rowSanta) + ',' + str(colSanta)
			if position not in (santa_grid and robo_grid):
				santa_grid[position] = 1
		else:
			rowRobo += 1
			position = str(rowRobo) + ',' + str(colRobo)
			if position not in (robo_grid and santa_grid):
				robo_grid[position] = 1
	elif char == '<':
		if turnSanta:
			rowSanta -= 1
			position = str(rowSanta) + ',' + str(colSanta)
			if position not in (santa_grid and robo_grid):
				santa_grid[position] = 1
		else:
			rowRobo -= 1
			position = str(rowRobo) + ',' + str(colRobo)
			if position not in (robo_grid and santa_grid):
				robo_grid[position] = 1
	elif char == '^':
		if turnSanta:
			colSanta += 1
			position = str(rowSanta) + ',' + str(colSanta)
			if position not in (santa_grid and robo_grid):
				santa_grid[position] = 1
		else:
			colRobo += 1
			position = str(rowRobo) + ',' + str(colRobo)
			if position not in (robo_grid and santa_grid):
				robo_grid[position] = 1
	elif char == 'v':
		if turnSanta:
			colSanta -= 1
			position = str(rowSanta) + ',' + str(colSanta)
			if position not in (santa_grid and robo_grid):
				santa_grid[position] = 1
		else:
			colRobo -= 1
			position = str(rowRobo) + ',' + str(colRobo)
			if position not in (robo_grid and santa_grid):
				robo_grid[position] = 1
	turnSanta = not turnSanta

print(len(santa_grid)+len(robo_grid)-1)