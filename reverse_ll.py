def reverse_linked_list(head):
	cur = head
	prev = None
	while cur is not None:
		nx = cur.next
		cur.next = prev
		prev = cur
		cur = nx
	return prev

def rec_reverse_linked_list(head, prev=None):
	if head is None:
		return prev
	nx = head.next
	head.next = prev
	return rec_reverse_linked_list(nx, head)