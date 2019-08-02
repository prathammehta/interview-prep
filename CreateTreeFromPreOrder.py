# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
import sys
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def get_pre_index():
	return generate_tree.pre_index

def increment_pre_index():
	generate_tree.pre_index += 1

def generate_tree(pre, key, min, max, size):

	if get_pre_index() >= len(pre):
		return None

	root = None

	if key > min and key < max:

		root = Node(key)
		increment_pre_index()	
		
		if get_pre_index() < size:
			root.left = generate_tree(pre, pre[get_pre_index()], min, key, size)	
			root.right = generate_tree(pre, pre[get_pre_index()], key, max, size)

	return root


def preorder(root):
	if root == None:
		return
	
	print(root.key)
	preorder(root.left)
	preorder(root.right)


generate_tree.pre_index = 0
pre = [10, 5, 1, 7, 40, 50]
size = len(pre)
root = generate_tree(pre, pre[0], -sys.maxsize, sys.maxsize, size)
preorder(root)

