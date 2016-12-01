def main():
	fp = open('day1a_input.txt')
	commandList = fp.readline().strip().split(', ')

	movement = [{'x': 0, 'y': 1}, {'x': 1, 'y': 0}, {'x': 0, 'y': -1}, {'x': -1, 'y': 0}]

	direction = 0
	x = 0
	y = 0

	for command in commandList:
		if(command[0] == 'L'):
			direction = (direction + 4 - 1) % 4
		else:
			direction = (direction + 1) % 4

		distance = int(command[1:])

		x += distance * movement[direction]['x']
		y += distance * movement[direction]['y']

	totalDistance = abs(x) + abs(y)
	print(totalDistance)


main()

