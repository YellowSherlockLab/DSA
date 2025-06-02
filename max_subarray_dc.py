def max_crossing_sum(arr, left, mid, right):
	ls, rs = float("-inf"), float("-inf")

	total = 0
	for i in range(mid, left-1, -1):
		total += arr[i]
		ls = max(ls, total)

	total = 0
	for i in range(mid+1, right+1):
		total += arr[i]
		rs = max(rs, total)

	return ls + rs

def max_subarray_dc(arr, left, right):
	if left == right:
		return arr[left]

	mid = (left + right)//2

	leftmax = max_subarray_dc(arr, left, mid)
	rightmax = max_subarray_dc(arr, mid+1, right)
	crossmax = max_crossing_sum(arr, left, mid, right)

	return max(leftmax, rightmax, crossmax)

def max_subarray(arr):
	return max_subarray_dc(arr, 0, len(arr)-1)