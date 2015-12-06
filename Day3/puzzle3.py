f = open("input.txt", 'r')
data = f.read()

uniqueHouses = 0
row = 0
col = 0

house_grid = {"0,0": 1}
for char in data:
	if char == '>':
		row += 1
		position = str(row) + ',' + str(col)
		if position not in house_grid:
			house_grid[position] = 1
	elif char == '<':
		row -= 1
		position = str(row) + ',' + str(col)
		if position not in house_grid:
			house_grid[position] = 1
	elif char == '^':
		col += 1
		position = str(row) + ',' + str(col)
		if position not in house_grid:
			house_grid[position] = 1
	elif char == 'v':
		col -= 1
		position = str(row) + ',' + str(col)
		if position not in house_grid:
			house_grid[position] = 1

print(len(house_grid))