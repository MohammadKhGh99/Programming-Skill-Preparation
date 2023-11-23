"""
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.

Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 ,so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 ,so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
Example 2:

Input: nums = [1,1,2,3]
Output: [1,3,3]

Constraints:
2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
"""


class Solution(object):
	def decompressRLElist(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		decompressed_list = []
		for i in range(0, len(nums), 2):
			# make a temporary list that contains just nums[i + 1] elements with length of nums[i], then add it to decompressed_list
			decompressed_list += [nums[i + 1] for _ in range(nums[i])]
		return decompressed_list


if __name__ == "__main__":
	solution = Solution()
	nums1 = [1, 2, 3, 4]
	print(" Input: " + str(nums1))
	print("Output: " + str(solution.decompressRLElist(nums1)))
	print()
	
	nums2 = [1, 1, 2, 3]
	print(" Input: " + str(nums2))
	print("Output: " + str(solution.decompressRLElist(nums2)))
	
	
