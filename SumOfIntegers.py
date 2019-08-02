# https://www.geeksforgeeks.org/ways-to-write-n-as-sum-of-two-or-more-positive-integers/

def sum_of_integers(num):
	possibilites = [0 for _ in range(num + 1)]
	possibilites[0] = 1

	for i in range(1,num):
		for j in range(i, num+1):
			possibilites[j] = possibilites[j] + possibilites[j - i]
		pass

	return possibilites[num]

print(sum_of_integers(5))
