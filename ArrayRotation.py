# Program to rotate an array
# https://practice.geeksforgeeks.org/problems/rotate-and-delete/0
# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
# Output = [3, 4, 5, 6, 7, 1, 2]

def rotateArray(a, n):
	for x in range(0,n):
		a.append(a.pop(0))
		pass
	return a
	


print(rotateArray([1,2,3,4,5,6,7],2))