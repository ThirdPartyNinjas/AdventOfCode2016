import hashlib

def main():
	input = 'abbhdwsy'
	password = ''
	count = 0
	index = 0

	while count < 8:
		hash = hashlib.md5((input + str(index)).encode('utf-8')).hexdigest()

		if(hash[:5] == '00000'):
			password += hash[5]
			count += 1

		index += 1

	print(password)

main()
