
def find_max_sum(array):
	max_sum = 0
	max_ending_here = 0
	for index in range(0,len(array)):
		max_ending_here += array[index]
		if max_ending_here < -1:
			max_ending_here = 0
		if max_ending_here > max_sum:
			max_sum = max_ending_here
		
	print(max_sum)

	


find_max_sum([-2, -3, -4, -1, -2, -1, -5, -3])