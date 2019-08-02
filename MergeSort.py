# Merge sort

def merge (a, b):
	m = len(a)
	n = len(b)
	p = m + n
	c = [0] * p
	i = 0
	j = 0
	for k in range(0, p):
		if i == m:
			c[k] = b[j]
			j += 1
		elif j == n:
			c[k] = a[i]
			i += 1
		elif a[i] < b[j]:
			c[k] = a[i]
			i += 1
		else:
			c[k] = b[j]
			j += 1

	return c




def merge_sort(array):
	if len(array) <= 1:
		return array
	else:
		mid_point = int((len(array)+1)/2)
		return merge(merge_sort(array[:mid_point]), merge_sort(array[mid_point:]))


print(merge_sort([4,3,1,6,7,1,1,8]))