"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be
 placed at the end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

Constraints:
1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""


class Solution(object):
	def relativeSortArray(self, arr1, arr2):
		"""
		:type arr1: List[int]
		:type arr2: List[int]
		:rtype: List[int]
		"""
		# we count each element in arr1
		dic = {}
		for i in range(len(arr1)):
			if arr1[i] not in dic:
				dic[arr1[i]] = 1
			else:
				dic[arr1[i]] += 1
		
		# we make the wanted occurrence from each element and add them to the result array
		res = []
		for key in arr2:
			res += ([key] * dic[key])
		
		# sort the remain elements
		remains = []
		for x in arr1:
			if x not in arr2:
				remains.append(x)
		remains = sorted(remains)
		return res + remains


if __name__ == '__main__':
	solution = Solution()
	arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
	arr2 = [2, 1, 4, 3, 9, 6]
	print(f"Input: arr1={arr1}, arr2={arr2}")
	print(f"Output: {solution.relativeSortArray(arr1, arr2)}")
	print()
	
	arr1 = [28, 6, 22, 8, 44, 17]
	arr2 = [22, 28, 8, 6]
	print(f"Input: arr1={arr1}, arr2={arr2}")
	print(f"Output: {solution.relativeSortArray(arr1, arr2)}")
	print()
	
	arr1 = [943, 790, 427, 722, 860, 550, 225, 846, 715, 320]
	arr2 = [943, 715, 427, 790, 860, 722, 225, 320, 846, 550]
	print(f"Input: arr1={arr1}, arr2={arr2}")
	print(f"Output: {solution.relativeSortArray(arr1, arr2)}")
	
	arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
	arr2 = [2, 42, 38, 0, 43, 21]
	print(f"Input: arr1={arr1}, arr2={arr2}")
	print(f"Output: {solution.relativeSortArray(arr1, arr2)}")
