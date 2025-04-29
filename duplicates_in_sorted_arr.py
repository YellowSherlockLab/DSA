def findDups(nums):
	""" This function works to return number of unique elements in a list, and to in place 
	modify the lest such that it only contains the unique elements, and the remaining indices are filled
	with the '_' character """

	# Initialise slow and fast pointers
	s, f = 0, 1
	while f < len(nums):
		# If the values at the two pointer indices are different
		# change the value at the index after the slow pointer to value at fast index
		# increment both pointers
		if nums[s] != nums[f]:
			nums[s+1] = nums[f]
			s += 1
			f += 1
		# If the values at pointer indices are the same
		# Only increment the fast pointer
		else:
			f += 1
	# Start at the index after the slow pointer.
	# This is also number of unique elements
	k = s+1
	for i in range(k,len(nums)):
		# Replace every element after the unique ones with '_'
		nums[i] = "_"
	return k, nums

def find2Dups(nums):
	""" This function works to modify a list of numbers (ints) inplace such that a number may be repeated only once
	The numbers after this treatment are replaced with the character '_'"""
	# Initialise both slow and fast at 2, since two duplicates are allowed
	s, f = 2, 2
	while f < len(nums):
		# If value at fast is not the same as value at slow-2, replace the value at slow with value at fast
		# Increment both pointers
		if nums[s-2] != nums[f]:
			nums[s] = nums[f]
			s += 1
			f += 1
		# If values at slow and fast are the same, increment only fast
		else:
			f += 1
	# Start at the index of the slow pointer (since we are allowed 2 duplicates)
	k = s
	for i in range(k, len(nums)):
		# Replace every element from k with '_'
		nums[i] = "_"

	return nums

nums = [0,0,0,1,1,1,2,3]
numUnique, modArr = findDups(nums)
print(f"Number of unique elemets is {numUnique} and modified array is {modArr}")


nums = [0,0,0,1,1,1,2,2,3]
modArr2 = find2Dups(nums)
print(f"Modified array is {modArr2}")