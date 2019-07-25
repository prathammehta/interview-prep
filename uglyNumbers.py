# https://www.geeksforgeeks.org/ugly-numbers/

def generateUgly(n):
	uglyNumberGenerated = 1
	uglyNumbers = [0,1]
	index = 2
	while uglyNumberGenerated<n:
		isUgly = False
 
		if index % 5 == 0 and uglyNumbers[int(index/5)] == 1:
			isUgly = True

		if index % 3 == 0 and uglyNumbers[int(index/3)] == 1:
			isUgly = True

		if index % 2 == 0 and uglyNumbers[int(index/2)] == 1:
			isUgly = True

		if isUgly == True:
			uglyNumbers.append(1)
			uglyNumberGenerated += 1
		else:
			uglyNumbers.append(0)

		index +=1

	return index-1


print(generateUgly(292))
