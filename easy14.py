"""
You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:
m is greater than 1.
s1 = s0 + 1.
The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1,
and so on up to s[m - 1] - s[m - 2] = (-1)m.
Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [2,3,4,3,4]
Output: 4
Explanation: The alternating subarrays are [3,4], [3,4,3], and [3,4,3,4]. The longest of these is [3,4,3,4], which is of length 4.

Example 2:
Input: nums = [4,5,6]
Output: 2
Explanation: [4,5] and [5,6] are the only two alternating subarrays. They are both of length 2.

Constraints:
2 <= nums.length <= 100
1 <= nums[i] <= 104
"""


class Solution(object):
	def alternatingSubarray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) < 2:
			return None
		longest_subarray = -1
		# check the condition when the initial length is 2
		cur_subarray = nums[:2]
		if cur_subarray[1] == cur_subarray[0] + 1:
			longest_subarray = 2
		else:
			cur_subarray = cur_subarray[1:]
		
		for i in range(2, len(nums)):
			# this check the condition when we want to add an element to the subarray which his index is even
			if len(cur_subarray) % 2 == 0:
				# if it fulfills the wanted condition
				if nums[i] - cur_subarray[-1] == -1:
					cur_subarray.append(nums[i])
				else:
					longest_subarray = max(longest_subarray, len(cur_subarray))
					if nums[i] - cur_subarray[-1] == 1:
						cur_subarray = [cur_subarray[-1], nums[i]]
					else:
						cur_subarray = [nums[i]]
			# this check the condition when we want to add an element to the subarray which his index is odd
			else:
				# if it fulfills the wanted condition
				if nums[i] - cur_subarray[-1] == 1:
					cur_subarray.append(nums[i])
				else:
					# if the current array doesn't fulfill the wanted condition and its length is 1
					if len(cur_subarray) == 1:
						cur_subarray = [nums[i]]
						continue
					longest_subarray = max(longest_subarray, len(cur_subarray))
					if nums[i] - cur_subarray[-1] == 1:
						cur_subarray = [nums[i]]
					else:
						cur_subarray = [cur_subarray[-1], nums[i]]
		
		return max(longest_subarray, len(cur_subarray)) if len(cur_subarray) > 1 else longest_subarray


if __name__ == '__main__':
	solution = Solution()
	
	nums = [21, 9, 5]
	print(f"Input: nums = {nums}")
	print(f"Output: {solution.alternatingSubarray(nums)}")
	print()
	
	nums = [4, 5, 6]
	print(f"Input: nums = {nums}")
	print(f"Output: {solution.alternatingSubarray(nums)}")
