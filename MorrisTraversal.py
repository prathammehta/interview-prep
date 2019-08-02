# Morris BST traversal

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def morris(root):
	current = root
	while current != None:

		if current.left == None:
			print(current.key)
			current = current.right

		else:
			pred = current.left
			while pred.right != None and pred.right != current:
				pred = pred.right

			if pred.right == None:
				pred.right = current
				current = current.left
			else:
				pred.right = None
				print(current.key)
				current = current.right



root = Node(10)
root.left = Node(5)
root.left.left = Node(-2)
root.left.left.right = Node(2)
root.left.left.right.left = Node(-1)
root.left.right = Node(6)
root.left.right.right = Node(8)
root.right = Node(30)
root.right.right = Node(40)

morris(root)
