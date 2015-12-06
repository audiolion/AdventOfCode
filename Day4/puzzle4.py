import hashlib

secret_key = "iwrupvqb"
test = 1
while True:
	m = hashlib.md5()
	m.update((secret_key + str(test)).encode('utf-8'))
	digest = m.hexdigest()
	if digest[0:6] == "000000":
		print(digest)
		break
	test += 1

print(secret_key + str(test))