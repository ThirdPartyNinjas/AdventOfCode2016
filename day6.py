import string

def main():
	with open('day6_input.txt') as file:
		dictionaries = [{}, {}, {}, {}, {}, {}, {}, {}]
		for i in range(8):
			for c in string.ascii_lowercase:
				dictionaries[i][c] = 0

		for line in file:
			for i in range(8):
				dictionaries[i][line[i]] += 1

		maxMessage = []
		minMessage = []

		for i in range(8):
			maxMessage.append(max(dictionaries[i].items(), key=lambda k: k[1])[0])
			minMessage.append(min(dictionaries[i].items(), key=lambda k: k[1])[0])

		print(maxMessage)
		print(minMessage)
main()
