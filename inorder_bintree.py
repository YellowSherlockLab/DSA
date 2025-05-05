def inorder_traversal(root, mode="iterative"):
	res = []
	if mode == "iterative":
		cur = root
		stack = []
		while cur or stack:
		while cur:
		stack.append(cur)
		cur = cur.left
		cur = stack.pop()
		res.append(cur.val)
		cur = cur.right
		return res

	if mode == "recursive":
		def traverse(node):
			if node:
				traverse(node.left)
				res.append(node.val)
				traverse(node.right)
		traverse(root)
		return res