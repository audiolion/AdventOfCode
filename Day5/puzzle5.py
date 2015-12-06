def is_nice(text):
	vowels = "aeiou"
	bad_strings = ["ab", "cd", "pq", "xy"]

	num_vowels = 0
	for char in vowels:
		for char2 in text:
			if char == char2:
				num_vowels += 1

	last_char = '0'
	double_letters = False
	for char in text:
		if last_char == char:
			double_letters = True
		last_char = char

	bad_string = False
	for element in bad_strings:
		if element in text:
			bad_string = True

	if(num_vowels > 2
		and	double_letters == True
		and bad_string == False):
		return True
	else:
		return False


f = open("input.txt", 'r')
data = f.read()
tokenized = data.split("\n")

nice_strings = 0
for token in tokenized:
	if is_nice(token):
		nice_strings += 1

print(nice_strings)