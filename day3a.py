def main():
	with open('day3_input.txt') as f:
		count = 0

		for line in f:
			n1, n2, n3 = map(int, line.split())

			if(n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1):
				count += 1

		print(count)

main()
