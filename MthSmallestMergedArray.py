import heapq
def mth_smallest(arrs, m):
	heap = []
	for i,arr in enumerate(arrs):
		heap.append((arr[0],i))


	heapq.heapify(heap)
	indexes = [1] * len(arrs)
	element = None
	for _ in range(m - 1):
		element = heapq.heappop(heap)
		min = float('inf')
		min_arr_index = None
		for i,arr in enumerate(arrs):
			if len(arr) > indexes[i]:
				if min > arr[indexes[i]]:
					min = arr[indexes[i]]
					min_arr_index = i

		print(indexes)

		if min_arr_index != None:
			heapq.heappush(heap, (arrs[min_arr_index][indexes[min_arr_index]], min_arr_index))
			indexes[min_arr_index] += 1

	print(heap[0][0])





mth_smallest([[1, 3, 20], [2, 4, 6]], 6)