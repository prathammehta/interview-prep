store = {}

def find_longest_sequence(arr1, arr2,acc1, acc2, i1, i2):
	global store

	key = str(acc1) + '-' + str(acc2) + '-' + str(i1) + '-' + str(i2)

	if key in store:
		# print('hit')
		return store[key]

	send1 = acc1.copy()
	if i1 < len(arr1):
		send1.append(arr1[i1])

	send2 = acc2.copy()
	if i2 < len(arr2):
		send2.append(arr2[i2])

	if acc2 == acc1 and len(acc1)>0:
		# print(acc1, acc2)
		store[key] = len(acc1)
		return len(acc1)
	
	elif i1 >= len(arr1) and i2 >= len(arr2):
		store[key] = 0
		return 0
	
	elif i1 >= len(arr1):
		return max(find_longest_sequence(arr1, arr2, acc1, send2, i1, i2+1),find_longest_sequence(arr1, arr2, acc1, acc2, i1, i2+1))
	
	elif i2 >= len(arr2):
		return max(find_longest_sequence(arr1, arr2, send1, acc2, i1+1, i2),find_longest_sequence(arr1, arr2, acc1, acc2, i1+1, i2))
	
	else:
		return max(find_longest_sequence(arr1, arr2, send1, acc2, i1+1, i2),find_longest_sequence(arr1, arr2, acc1, acc2, i1, i2+1),find_longest_sequence(arr1, arr2, acc1, send2, i1+1, i2),find_longest_sequence(arr1, arr2, acc1, acc2, i1, i2+1),)


print(find_longest_sequence([1,2,7,3,5,6], [7,3,8,5,9,6],[], [], 0, 0))