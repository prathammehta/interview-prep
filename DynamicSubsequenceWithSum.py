# https://www.geeksforgeeks.org/subsetsumproblemdp25/


def calculate_sum(array, n, target, mem):
	key = str(n) + str(target)
	if key in mem:
		print('HIT')
		return mem[key]
	if target == 0:
		mem[key] = True
		return True
	elif target < 0:
		mem[key] = False
		return False
	elif n == 0:
		mem[key] = False
		return False
	elif array[n-1] > target:
		return calculate_sum(array, n-1, target, mem)
	else:
		res1 = calculate_sum(array, n-1, target, mem)
		res2 = calculate_sum(array, n-1, target - array[n-1], mem)
		if res1 == True or res2 == True:
			mem[key] = True
			return True

		mem[key] = False
		return False
	
	

arr = [3, 34, 12, 2, 5, 4]
print(calculate_sum(arr,len(arr),9, {}))

