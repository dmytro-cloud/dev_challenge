TOTAL_PRIORITY = 0

f = open('Day3_input.txt', 'r')

for line in f:
	set1 = set()
	set2 = set()
	for i in range(len(line.strip())):
		if i > len(line.strip()) / 2 - 1:
			set2.add(line[i])
		else:
			set1.add(line[i])
	inter = set1.intersection(set2).pop()
	if (ord(inter) > 90):
		TOTAL_PRIORITY += ord(inter) - 96
	else:
		TOTAL_PRIORITY += ord(inter) - 64 + 26
print(TOTAL_PRIORITY)