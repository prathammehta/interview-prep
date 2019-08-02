# https://www.geeksforgeeks.org/count-palindromic-subsequence-given-string/

mem = {}

def find_sub_sequence(given_string, start, end, acc):
	global mem
	key = str(start) + ' ' + str(acc)
	if key in mem:
		print('HIT')
		return mem[key]
		
	if acc == acc[::-1] and len(acc) > 1 and start>end:
		print(start, acc)
		return 1

	sum = 0
	if start <= end:
		sum = sum + find_sub_sequence(given_string, start + 1, end, acc) + find_sub_sequence(given_string, start + 1, end, acc + given_string[start])

	mem[key] = sum
	return sum

string = 'aaaa'

print(find_sub_sequence(string,0,len(string)-1,"") + len(string))