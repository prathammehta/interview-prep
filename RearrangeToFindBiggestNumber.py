# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
def compareNumbers(num1, num2):
	genNum1 = int(str(num1) + str(num2))
	genNum2 = int(str(num2) + str(num1))
	if(genNum1 > genNum2):
		return 0
	else:
		return 1


def reorderArray(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if  compareNumbers(arr[j],arr[j+1]) == 1:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)



reorderArray([1, 34, 3, 98, 9, 76, 45, 4])