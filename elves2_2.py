f = open('innput_elves.csv', 'r')

def winner2(p1, p2):
	p1 = ord(p1) - 65
	if p2 == 'Y':
		return p1 + 1 + 3
	if p2 == 'Z':
		return (p1 + 1) % 3 + 1 + 6

	return (p1 + 2) % 3 + 1

TOTAL = 0

for line in f:
	pair = []
	for s in line.split(' '):
		pair.append(s.strip())
	TOTAL += winner2(*pair)

print(TOTAL)