# https://www.geeksforgeeks.org/transform-bst-sum-tree/

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.visited = False


def convert_to_gst(root):
	s = []
	current_sum = 0
	s.append(root)
	while len(s) > 0:
		if s[-1].right != None and s[-1].right.visited == False:
			s.append(s[-1].right)
		else:
			current_node = s.pop()
			current_node.visited = True
			temp_sum = current_sum
			current_sum += current_node.key
			current_node.key = temp_sum
			if current_node.left != None:
				s.append(current_node.left)

def inorder(root):
	if root == None:
		return
	
	inorder(root.left)
	print(root.key)
	inorder(root.right)

def insert(root, key):
	if root == None:
		return Node(key)

	if key < root.key:
		root.left = insert(root.left, key)

	if key > root.key:
		root.right = insert(root.right, key)

	return root

root = Node(11)
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 7)
root = insert(root, 29)
root = insert(root, 15)
root = insert(root, 40)
root = insert(root, 35)

convert_to_gst(root)
inorder(root)
