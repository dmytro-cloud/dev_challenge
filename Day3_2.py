TOTAL_PRIORITY = 0

f = open('Day3_input.txt', 'r')

counter = 0
set1 = set()
set2 = set()
set3 = set()
for line in f:
	counter += 1
	if counter == 1:
		set1 = set(line.strip())
	if counter == 2:
		set2 = set(line.strip())
	# for i in range(len(line.strip())):
	# 	if i > len(line.strip()) / 2 - 1:
	# 		set2.add(line[i])
	# 	else:
	# 		set1.add(line[i])
	# inter = set1.intersection(set2).pop()

	if counter == 3:
		set3 = set(line.strip())
		inter = set1.intersection(set2).intersection(set3).pop()
		if (ord(inter) > 90):
			TOTAL_PRIORITY += ord(inter) - 96
		else:
			TOTAL_PRIORITY += ord(inter) - 64 + 26	
		counter = 0
print(TOTAL_PRIORITY)