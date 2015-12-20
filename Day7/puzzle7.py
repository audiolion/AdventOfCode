data = open("input.txt", 'r').read()
data = data.split('\n')

circuit = {}
memo = {}

for instruction in data:
	instruction = instruction.split(" -> ")
	if len(instruction) > 1:
		if instruction[1] not in circuit:
			circuit[instruction[1]] = instruction[0]

def command(instruction, memoKey):
	if memoKey in memo:
		return memo[memoKey]
	if "AND" in instruction:
		wires = instruction.split(" AND ")
		memo[wires[0]] = command(wires[0], instruction)
		memo[wires[1]] = command(wires[1], instruction)
		return memo[wires[0]] & memo[wires[1]]
	elif "OR" in instruction:
		wires = instruction.split(" OR ")
		memo[wires[0]] = command(wires[0], instruction)
		memo[wires[1]] = command(wires[1], instruction)
		return memo[wires[0]] | memo[wires[1]]
	elif "NOT" in instruction:
		wires = instruction.split("NOT ")
		memo[wires[1]] = command(wires[1], instruction)
		return ~ memo[wires[1]] & 65355
	elif "LSHIFT" in instruction:
		wires = instruction.split(" LSHIFT ")
		memo[wires[0]] = command(wires[0], instruction)
		return memo[wires[0]] << int(wires[1])
	elif "RSHIFT" in instruction:
		wires = instruction.split(" RSHIFT ")
		memo[wires[0]] = command(wires[0], instruction) 
		return memo[wires[0]] >> int(wires[1])
	elif instruction in circuit:
		return command(circuit[instruction], instruction)
	else:
		return int(instruction)

print("a:",command(circuit['a'], "a"))
memo = {}
memo['b'] = 3176
print("a with override:", command(circuit['a'], "a"))