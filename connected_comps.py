def count_connected(graph):
	visited = set()
	count = 0
	for node in graph:
		if explore(graph, node, visited):
			count += 1
	return count

def explore(graph, node, visited):
	if node in visited:
		return False
	visited.add(node)
	for neighbour in node:
		explore(graph, neighbour, visited)
	return True