# https://www.geeksforgeeks.org/program-nth-catalan-number/

#c0 = 1
#cn+1 = 

def numberOfCombinations(n,store):
	key = str(n)
	if n == 0:
		return 1
	elif key in store:
		return store[key]
	else:
		result = 0
		for i in range(0,n):
			result = result + numberOfCombinations(i,store) * numberOfCombinations(n-1-i,store)
			pass
		store[key] = result
		return result


print(numberOfCombinations(15,{}))

