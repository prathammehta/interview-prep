def build_temp(pat):
	T = [0] * len(pat)

	j = 0
	i = 1

	while i < len(T):
		if pat[i] == pat[j]:
			T[i] = j + 1
			i += 1
			j += 1
		else:
			if j == 0:
				T[i] = 0
				i += 1
			else:
				j = T[j-1]

	return T

def find_index(S,T):
	temp = build_temp(T)

	i = 0
	j = 0
	while i < len(S) and j < len(T):
		if S[i] == T[j]:
			i += 1
			j += 1
		else:
			if j == 0:
				i += 1
			else:
				j = temp[j - 1]

		if j == len(T):
			return i - len(T)

	return -1




print(find_index('abcxabcdabcdabcy','abcdabcy'))