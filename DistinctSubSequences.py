# https://www.geeksforgeeks.org/count-distinct-subsequences/

distinct_sequences = {}

def count_distinct_subseq(given_string, length, start, acc, mem):
	key = str(start) + '-' + str(acc)
	if start > length:
		return 0

	if start == length:
		if acc in distinct_sequences:
			return 0
		else:
			distinct_sequences[acc] = 1
			return 1


	sum = count_distinct_subseq(given_string, length, start+1, acc) + count_distinct_subseq(given_string, length, start+1, acc + given_string[start])
	return sum


string = 'ggg'
print(count_distinct_subseq(string, len(string), 0, ''))