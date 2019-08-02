# Merge N sorted Arrays

import math

class HeapNode:
	def __init__(self,key,array):
		self.key = key
		self.array = array

	def __repr__(self):
		return '['+str(self.key)+', '+str(self.array)+']'

def heap_swap(heap, index_1, index_2):
	temp = heap[index_1]
	heap[index_1] = heap[index_2]
	heap[index_2] = temp

def heap_get_parent_index(index):
	return math.ceil(index/2) - 1

def heap_get_left_child_index(index):
	return index * 2 + 1

def heap_get_right_child_index(index):
	return index * 2 + 2

def heapify_up(heap):
	index = len(heap) - 1
	while heap_get_parent_index(index) >= 0:
		if heap[index].key < heap[heap_get_parent_index(index)].key:
			heap_swap(heap, index, heap_get_parent_index(index))
			index = heap_get_parent_index(index)
		else:
			return


def heapify_down(heap):
	index = 0
	while heap_get_left_child_index(index) < len(heap):
		min_index = heap_get_left_child_index(index)
		if heap_get_right_child_index(index) < len(heap):
			if heap[min_index].key > heap[heap_get_right_child_index(index)].key:
				min_index = heap_get_right_child_index(index)

		if heap[index].key > heap[min_index].key:
			heap_swap(heap, index, min_index)
			index = min_index
		else:
			return

def heap_extract_min(heap):
	min_element = heap[0]
	heap_swap(heap, 0, len(heap)-1)
	heap.pop()
	heapify_down(heap)
	return min_element


def heap_insert(heap, key, array_index):
	heap.append(HeapNode(key, array_index))
	heapify_up(heap)


def merge_arrays(arrays):
	k = len(arrays)
	active_indices = [0] * k
	sorted_array = []
	heap = []
	for index in range(0,k):
		heap_insert(heap, arrays[index][0], index)

	while len(heap) > 0:
		min_element = heap_extract_min(heap)
		sorted_array.append(min_element.key)
		active_indices[min_element.array] += 1
		if active_indices[min_element.array] < len(arrays[min_element.array]):
			heap_insert(heap, arrays[min_element.array][active_indices[min_element.array]], min_element.array)


	return sorted_array


print(merge_arrays([[1, 3, 5, 7],[2, 4, 6, 8],[0, 9, 10, 11]]))
