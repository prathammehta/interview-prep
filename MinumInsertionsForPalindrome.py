# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/

def find_number_of_charecters(string, start, end, cost):
	# print(string[start:end+1], start, end, cost)
	if start >= end:
		return cost
	
	if string[start] == string[end]:
		return find_number_of_charecters(string, start+1, end-1, cost)

	return min(find_number_of_charecters(string, start + 1, end, cost + 1), find_number_of_charecters(string, start, end - 1, cost + 1))