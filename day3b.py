def is_triangle(n0, n1, n2):
	if(n0 + n1 > n2 and n0 + n2 > n1 and n1 + n2 > n0):
		return True
	return False

def main():
	with open('day3_input.txt') as f:
		count = 0
		lineCount = 0

		for line in f:
			if(lineCount == 0):
				numbers = []

			numbers.extend(map(int, line.split()))

			lineCount += 1
			if(lineCount == 3):
				if(is_triangle(numbers[0], numbers[3], numbers[6])):
					count += 1
				if(is_triangle(numbers[1], numbers[4], numbers[7])):
					count += 1
				if(is_triangle(numbers[2], numbers[5], numbers[8])):
					count += 1
				lineCount = 0

		print(count)

main()
