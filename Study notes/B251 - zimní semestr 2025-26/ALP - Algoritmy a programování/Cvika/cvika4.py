def max2(nums):
	secondmax=sorted(nums)[-2]
	return (secondmax, nums.index(secondmax))
ns = [5, 3, 5, 2, 7, 7] # fail state

def max_k(nums, k):
	nums_tmp = list(nums)

	maxs = list()

	for i in range(0, k):
		tmp_max = float("-inf")
		for ii in range(0, len(nums)):
			if nums_tmp[ii] > tmp_max:
				tmp_max = nums_tmp[ii]
		for ii in range(0, len(nums)):
			if nums_tmp[ii] == tmp_max:
				nums_tmp[ii] = float("-inf")
		maxs.append(tmp_max)

	return (maxs[k - 1], nums.index(maxs[k - 1]))

print(max_k(ns, 3))