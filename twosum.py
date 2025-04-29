def twosum(nums, target):
	""" This function returns the indices of elements in the list that add up to the target
	If no such elements are found, it returns an empty list"""

	# Initialise an empty dict (hash map)
	comps = {}
	for i in range(len(nums)):
		# Find the difference between the current element and target
		comp = target - nums[i]
		# If the difference is a key in the hash map, return it's value and current index
		if comp in comps:
			return [comps[comp], i]
		# Add the current element as key to the hash map with its index as value
		comps[nums[i]] = i
	return []

nums = [2,0,6,3]
target = 9
print(twosum(nums, target))