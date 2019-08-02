class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def constBSTpre(arr):
	s = []
	root = Node(arr[0])
	s.append(root)
	n = len(arr)
	for i in range(1, n):
		temp = None
		while (s != [] and arr[i] > s[len(s) - 1].key):
			temp = s.pop()
			if temp != None:
				temp.right = Node(arr[i])
				s.append(temp.right)
			else :
				s[len(s) - 1].left = Node(arr[i])
				s.append(s[len(s) - 1].left)

	return root

def inorder(node):
	if node != None:
		inorder(node.left)
		print(node.key)
		inorder(node.right)

arr = [10, 5, 1, 7, 40, 50]

root = constBSTpre(arr)
inorder(root)