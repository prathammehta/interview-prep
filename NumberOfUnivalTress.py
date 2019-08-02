# https://www.youtube.com/watch?v=7HgsS8bRvjo

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def increment_count():
	recurse_unival.count += 1

def get_count():
	return recurse_unival.count

def recurse_unival(root):
	if root.left == None and root.right == None:
		print('no children', root.key)
		increment_count()
		return root.key

	elif root.right == None:
		if recurse_unival(root.left) == root.key:
			increment_count()
			return root.key
		else: 
			return -1

	elif root.left == None:
		if recurse_unival(root.right) == root.key:
			increment_count()
			return root.key
		else:
			return - 1

	elif recurse_unival(root.right) == root.key and recurse_unival(root.left) == root.key:
		increment_count()
		return root.key

	else:
		return -1



recurse_unival.count = 0
root = Node(3)
root.left = Node(2)
root.right = Node(1)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(6)

recurse_unival(root)
print(get_count())




