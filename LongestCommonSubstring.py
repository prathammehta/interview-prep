def longest_sub_string(a, b, i, j):
	if i >= len(a) or j >= len(b):
		return 0
	if a[i] == b[j]:
		return 1 + longest_sub_string(a,b,i+1,j+1)
	else:
		return max(longest_sub_string(a,b,i+1,j), longest_sub_string(a,b,i,j+1))


print(longest_sub_string('abcd','abcdef',0,0))