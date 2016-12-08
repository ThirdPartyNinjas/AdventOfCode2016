import re

def rect(w, h, pixels):
	for y in range(h):
		for x in range(w):
			pixels[y][x] = '#'

def rotateRow(row, offset, pixels):
	copy = [0 for i in range(50)]
	for i in range(50):
		copy[i] = pixels[row][i]
	for i in range(50):
		pixels[row][i] = copy[(i + 50 - offset) % 50]

def rotateColumn(column, offset, pixels):
	copy = [0 for i in range(6)]
	for i in range(6):
		copy[i] = pixels[i][column]
	for i in range(6):
		pixels[i][column] = copy[(i + 6 - offset) % 6]

def main():
	pixels = [['.' for x in range(50)] for y in range(6)]
	with open('day8_input.txt') as f:
		for line in f:
			numbers = [int(i) for i in re.findall('([0-9][0-9]*)', line)]

			if(line[:4] == 'rect'):
				rect(numbers[0], numbers[1], pixels)
			elif(line[:10] == 'rotate row'):
				rotateRow(numbers[0], numbers[1], pixels)
			else:
				rotateColumn(numbers[0], numbers[1], pixels)

	count = 0
	for y in range(6):
		for x in range(50):
			if(pixels[y][x] != '.'):
				count += 1

	for y in range(6):
		for x in range(50):
			print(pixels[y][x], end='')
		print('')

	print(count)

main()

