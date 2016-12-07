import re

def main():

	sum = 0

	with open('day4_input.txt') as f:
		for line in f:

			sectorId = int(re.findall('([0-9][0-9]*)', line)[0])
			checksum = line[-7:-2]

			characterDict = {}

			for c in line[:-8]:
				if(c.isalpha()):
					if(c in characterDict):
						characterDict[c] += 1
					else:
						characterDict[c] = 1

			sortedData = sorted(characterDict.items(), key=lambda x: (-x[1], x[0]))

			if(len(sortedData) < 5):
				continue
			if(checksum[0] == sortedData[0][0] and
				checksum[1] == sortedData[1][0] and
				checksum[2] == sortedData[2][0] and
				checksum[3] == sortedData[3][0] and
				checksum[4] == sortedData[4][0]):
				sum += sectorId

	print(sum)

main()
