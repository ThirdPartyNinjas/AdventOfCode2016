def main():
	fp = open('day1a_input.txt')
	commandList = fp.readline().strip().split(', ')

	movement = [{'x': 0, 'y': 1}, {'x': 1, 'y': 0}, {'x': 0, 'y': -1}, {'x': -1, 'y': 0}]

	direction = 0
	x = 0
	y = 0
	locations = set()

	for command in commandList:
		if(command[0] == 'L'):
			direction = (direction + 4 - 1) % 4
		else:
			direction = (direction + 1) % 4

		distance = int(command[1:])

		for _ in range(distance):
			x += movement[direction]['x']
			y += movement[direction]['y']

			location = '%d|%d' % (x, y)
			if(location in locations):
				totalDistance = abs(x) + abs(y)
				print(totalDistance)
				return

			locations.add(location)

main()
