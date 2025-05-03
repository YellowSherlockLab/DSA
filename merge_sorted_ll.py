def merge_sorted_ll(head1, head2):
	sentinel = Node(-1)
	tail = sentinel
	while head1 is not None and head2 is not None:
		if head1.val < head2.val:
			tail.next = head1
			head1 = head1.next
		else:
			tail.next = head2
			head2 = head2.next
		tail = tail.next
	tail.next = head1 if head1 is not None else head2
	return sentinel.next