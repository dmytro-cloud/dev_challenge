# Too lazy to write a parser for a 1 time thing
''' 
[T]     [Q]             [S]        
[R]     [M]             [L] [V] [G]
[D] [V] [V]             [Q] [N] [C]
[H] [T] [S] [C]         [V] [D] [Z]
[Q] [J] [D] [M]     [Z] [C] [M] [F]
[N] [B] [H] [N] [B] [W] [N] [J] [M]
[P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
[B] [W] [N] [P] [D] [V] [G] [L] [T]
 1   2   3   4   5   6   7   8   9 
'''

stack_1 = ['B', 'P', 'N', 'Q', 'H', 'D', 'R', 'T']
stack_2 = ['W', 'G', 'B', 'j', 't', 'v']
stack_3 = list('nrhdsVmq')
stack_4 = list('PZNMC')
stack_5 = list('DZB')
stack_6 = list('VCWZ')
stack_7 = list('GZNCVQLS')
stack_8 = list('LGJMDNV')
stack_9 = list('TPMFZCG')

docker = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]

f = open('Day5_input.txt', 'r')

how_many = 0
move_from = 0
move_to = 0
prev = ''
for line in f:
	for word in line.split(' '):
		if prev == 'move':
			how_many = int(word)
			prev = ''
		elif prev == 'from':
			move_from = int(word)
			prev = ''
		elif prev == 'to':
			move_to = int(word)
			prev = ''
		else:
			prev = word
	tmp = docker[move_from - 1][-how_many:]
	docker[move_from - 1] = docker[move_from - 1][:-how_many]
	print(how_many, tmp)
	docker[move_to - 1].extend(tmp)

for p in docker:
	print(p.pop(), end='')

