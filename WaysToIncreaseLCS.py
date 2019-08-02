# https://www.geeksforgeeks.org/count-ways-increase-lcs-length-two-strings-one/

# THIS IS WRONG!!

def find_lcs(str1, str2):
	lcs = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

	max_value = 0
	max_i = 0

	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			if str1[i-1] == str2[j-1]:
				lcs[i][j] = 1 + lcs[i-1][j-1]
			else:
				lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

			if lcs[i][j] > max_value:
				max_value = lcs[i][j]
				max_i = i

	return len(str1) - max_i + 1

print(find_lcs("abab","abc"))
	