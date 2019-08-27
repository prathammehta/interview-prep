def generate_temp(p):
	pat = list(p)
	temp = [0] * len(pat)

	j = 0
	i = 1
	while i < len(pat):
		if pat[i] == pat[j]:
			temp[i] = j + 1
			i += 1
			j += 1
		else:
			if j == 0:
				temp[i] = 0
				i+=1
			else:
				j = temp[j-1]

	return temp


def KMP(s, p):
	temp = generate_temp(p)

	i = 0
	j = 0
	while i<len(s) and j<len(p):
		if s[i] == p[j]:
			i+=1
			j+=1

		else:
			if j == 0:
				i+=1
				
			else:
				j = temp[j-1]

		if j == len(p):
			return i - len(p)

	return -1


print(KMP('abcxabcdabcdabcy','abcdabcy'))