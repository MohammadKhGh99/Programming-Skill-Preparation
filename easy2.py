"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
Given an integer n, return a list of two integers [a, b] where:
a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 9 = n.
Note that there are other valid answers as [8, 3] that can be accepted.

Constraints:
2 <= n <= 104
"""


class Solution(object):
	def getNoZeroIntegers(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		for x in range(1, n):
			if str(x).count('0') == 0 and str(n - x).count('0') == 0:
				return [x, n - x]


if __name__ == '__main__':
	solution = Solution()
	print("Input: 2")
	print("Output: " + str(solution.getNoZeroIntegers(2)))
	print()
	print("Input: 11")
	print("Output: " + str(solution.getNoZeroIntegers(11)))
	
