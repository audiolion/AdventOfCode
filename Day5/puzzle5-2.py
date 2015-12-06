def is_nice(text):
	sandwiched_letter = False
	repeated_pair = False
	for i in range(len(text)):
		if i+2 < len(text):
			if text[i] == text[i+2]:
				sandwiched_letter = True
			pair = text[i] + text[i+1]
			if pair in text[i+2:len(text)]:
				repeated_pair = True

	if repeated_pair and sandwiched_letter:
		return True
	else:
		return False

f = open("input.txt", 'r')
data = f.read()

tokenized = data.split('\n')

nice_strings = 0
for token in tokenized:
	if is_nice(token):
		nice_strings += 1

print(nice_strings)