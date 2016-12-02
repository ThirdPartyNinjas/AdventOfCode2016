def clamp(n, smallest, largest):
	return max(smallest, min(n, largest))

def main():
	x = 1
	y = 1

	movement = {'L' : {'x': -1, 'y': 0}, 'R' : {'x': 1, 'y': 0}, 'U' : {'x': 0, 'y': -1}, 'D' : {'x': 0, 'y': 1}}

	with open('day2a_input.txt') as f:
		for line in f:
			for c in line.strip():
				x = clamp(x + movement[c]['x'], 0, 2)
				y = clamp(y + movement[c]['y'], 0, 2)

			button = y * 3 + x + 1
			print(button, end='')

main()
