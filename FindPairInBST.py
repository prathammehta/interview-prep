# https://www.geeksforgeeks.org/find-pair-given-sum-bst/

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def value_exists_map(value):
	if value in find_sum.visited_values:
		return True
	else:
		return False

def add_value_map(value):
	find_sum.visited_values[value] = 1

def find_sum(root, sum):
	if root == None:
		return
	
	find_sum(root.left, sum)
	
	if value_exists_map(sum - root.key) == True:
		print('Elements found!', root.key, sum-root.key)
		return

	add_value_map(root.key)

	find_sum(root.right, sum)




find_sum.visited_values = {}
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

find_sum(root, 10)
