import math

def left_child_exists(heap, index):
	if get_left_child_index(index) < len(heap):
		return True
	return False

def right_child_exists(heap, index):
	if get_right_child_index(index) < len(heap):
		return True
	return False

def get_parent_index(index):
	return math.ceil(index/2) - 1

def get_left_child_index(index):
	return index * 2 + 1

def get_right_child_index(index):
	return index * 2 + 2

def swap(heap, index1, index2):
	temp = heap[index1]
	heap[index1] = heap[index2]
	heap[index2] = temp

def heapify_up(heap):
	index = len(heap) - 1
	while index > 0 and get_parent_index(index) >= 0:
		if heap[index] < heap[get_parent_index(index)]:
			swap(heap, index, get_parent_index(index))
		index = get_parent_index(index)

def heapify_down(heap):
	if len(heap) <= 0:
		return heap

	index = 0
	while left_child_exists(heap, index):
		min_index = get_left_child_index(index)
		if right_child_exists(heap, index):
			if heap[get_right_child_index(index)] < heap[min_index]:
				min_index = get_right_child_index(index)

		swap(heap, index, min_index)
		index = min_index


def insert(heap, item):
	heap.append(item)
	heapify_up(heap)

def print_smallest(heap):
	print(heap[0])

def remove_smallest(heap):
	heap[0] = heap[len(heap) - 1]
	heapify_down(heap)


created_heap = []
insert(created_heap, 9)
insert(created_heap, 7)
insert(created_heap, 5)
insert(created_heap, 3)
insert(created_heap, 1)
insert(created_heap, -21)
print(created_heap)
print_smallest(created_heap)
remove_smallest(created_heap)
print(created_heap)