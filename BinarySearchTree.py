# BST

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def insert(root, key):
	if root == None:
		return Node(key)

	if key < root.key:
		root.left = insert(root.left, key)

	if key > root.key:
		root.right = insert(root.right, key)

	return root

def levelorder(root):
	if root == None:
		return

	q = []
	q.append(root)

	while len(q) > 0:
		temp = q.pop(0)
		if temp.left != None:
			q.append(temp.left)
		if temp.right != None:
			q.append(temp.right)
		print(temp.key)



def preorder(root):
	if root == None:
		return
	
	print(root.key)
	inorder(root.left)
	inorder(root.right)

def inorder(root):
	if root == None:
		return
	
	inorder(root.left)
	print(root.key)
	inorder(root.right)


root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 40)
root = insert(root, 1)
root = insert(root, 7)
root = insert(root, 50)
inorder(root)
print('')
preorder(root)
print('')
levelorder(root)






		