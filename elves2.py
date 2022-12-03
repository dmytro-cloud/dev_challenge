f = open('innput_elves.csv', 'r')

def winner2(p1, p2):
	p1 = ord(p1)
	p2 = ord(p2) - 23
	if p1 - p2 == 0:
		return 3
	if p2 - p1 == 1 or p2 - p1 == -2:
		return 6
	return 0

TOTAL = 0

for line in f:
	pair = []
	for s in line.split(' '):
		pair.append(s.strip())
	TOTAL += winner2(*pair)
	TOTAL += ord(pair[1]) - ord('W')

print(TOTAL)