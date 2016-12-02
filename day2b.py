def clamp(n, smallest, largest):
	return max(smallest, min(n, largest))

def main():
	x = 0
	y = 2

	keypad = [['0', '0', '1', '0', '0'], ['0', '2', '3', '4', '0'], ['5', '6', '7', '8', '9'], ['0', 'A', 'B', 'C', '0'], ['0', '0', 'D', '0', '0']]

	movement = {'L' : {'x': -1, 'y': 0}, 'R' : {'x': 1, 'y': 0}, 'U' : {'x': 0, 'y': -1}, 'D' : {'x': 0, 'y': 1}}

	with open('day2a_input.txt') as f:
		for line in f:
			for c in line.strip():
				nx = clamp(x + movement[c]['x'], 0, 4)
				ny = clamp(y + movement[c]['y'], 0, 4)
				if(keypad[ny][nx] != '0'):
					x = nx
					y = ny

			print(keypad[y][x], end='')

main()
