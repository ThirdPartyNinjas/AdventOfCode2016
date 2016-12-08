import hashlib

def main():
	input = 'abbhdwsy'
	password = [' ', ' ', ' ' , ' ', ' ', ' ', ' ', ' ']
	count = 0
	increasing = 0

	while count < 8:
		hash = hashlib.md5((input + str(increasing)).encode('utf-8')).hexdigest()

		if(hash[:5] == '00000'):
			if(hash[5].isdigit()):
				index = int(hash[5])
				if(index < 8 and password[index] == ' '):
					password[index] = hash[6]
					count += 1

		increasing += 1

	print(password)

main()
