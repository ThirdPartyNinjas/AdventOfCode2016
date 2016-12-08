import re

def containsAbba(s):
	return re.search(r'([a-z])(?!\1)([a-z])\2\1', s) != None

def supportsTLS(words, hypernet):
	return containsAbba(words) and not(containsAbba(hypernet))

def supportsSSL(words, hypernet):
	matches = re.findall(r'(?=(([a-z])(?!\2)[a-z]\2))', words)

	for m in matches:
		aba = m[0]
		bab = aba[1] + aba[0] + aba[1]
		if(bab in hypernet):
			return True
	return False

def main():
	with open('day7_input.txt') as file:
		splitLines = [re.split(r'\[([^\]]+)\]', line.strip()) for line in file]
		joinedParts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in splitLines]

		print('Part One: ', sum(supportsTLS(words, hypernet) for words, hypernet in joinedParts))
		print('Part Two: ', sum(supportsSSL(words, hypernet) for words, hypernet in joinedParts))

main()
