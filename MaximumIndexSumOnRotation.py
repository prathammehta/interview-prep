# https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/

def findLargestSum(a):
	sumValue = 0
	maxSum = sumValue
	changeSumValue = 0
	numberOfRotations = 1
	
	for i in range(0,len(a)):
		sumValue = sumValue + i*a[i]
		changeSumValue = changeSumValue + a[i]
		pass

	for j in range(len(a)-1,-1,-1):
		sumValue = sumValue - ((len(a))*a[j]) + changeSumValue
		print(sumValue)

	

findLargestSum([1, 20, 2, 10])