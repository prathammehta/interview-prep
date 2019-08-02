# https://www.geeksforgeeks.org/super-ugly-number-number-whose-prime-factors-given-set/
import sys
def findSuperUglyNumber(primes, n):

	index = [0] * len(primes)
	uglies = [1]

	for i in range(1,n):
		min_value = sys.maxsize
		for j in range(0,len(primes)):
			possible_ugly = primes[j] * uglies[index[j]]
			if possible_ugly <= min_value:
				min_value = possible_ugly

		for j in range(0, len(primes)):
			possible_ugly = primes[j] * uglies[index[j]]
			if possible_ugly == min_value:
				index[j] += 1

		uglies.append(min_value)

	return uglies


print(findSuperUglyNumber([2,5],5))