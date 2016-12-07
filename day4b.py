import re

def decode(s, n):
	key = 'abcdefghijklmnopqrstuvwxyz'
	result = ''

	offset = ord('a')

	for c in s:
		if(c.isalpha()):
			i = (ord(c) - offset + n) % 26
			result += key[i]
		else:
			result += ' '

	return result

def main():
	with open('day4_input.txt') as f:
		for line in f:

			sectorId = int(re.findall('([0-9][0-9]*)', line)[0])
			roomCode = line[:re.search('(-[0-9])', line).start()]

			decoded = decode(roomCode, sectorId)

			if(decoded == 'northpole object storage'):
				print(sectorId)
				return
main()
