

l =  ['G', 'B', 'R', 'R', 'B', 'R', 'G']
letters = ['R', 'G']
insert_index = 0
for letter in letters:
	for i in range(insert_index, len(l)):
		if l[i] == letter:
			l[i], l[insert_index] = l[insert_index], l[i]
			insert_index += 1

print(l)
