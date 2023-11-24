"""
Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of
candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.
Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy.
The total amount of candy a person has is the sum of the number of candies in each box they have.
Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies
in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.

Example 1:
Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]

Example 2:
Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]

Example 3:
Input: aliceSizes = [2], bobSizes = [1,3]
Output: [2,3]

Constraints:
1 <= aliceSizes.length, bobSizes.length <= 104
1 <= aliceSizes[i], bobSizes[j] <= 105
Alice and Bob have a different total number of candies.
There will be at least one valid answer for the given input.
"""


class Solution(object):
	def fairCandySwap(self, aliceSizes, bobSizes):
		"""
		:type aliceSizes: List[int]
		:type bobSizes: List[int]
		:rtype: List[int]
		"""
		bob_sum = sum(bobSizes)
		alice_sum = sum(aliceSizes)
		# if both Alice and Bob have the same amount of candies in the beginning ,so we are done ,and we don't want to exchange any amount of candy
		if alice_sum == bob_sum:
			return [0, 0]
		
		alice_set = set(aliceSizes)
		bob_set = set(bobSizes)
		total = bob_sum + alice_sum
		for i in alice_set:
			if alice_sum - i < total // 2:
				if total // 2 - (alice_sum - i) in bob_set:
					return [i, total // 2 - (alice_sum - i)]
		return [0, 0]


if __name__ == "__main__":
	solution = Solution()
	
	aliceSizes = [1, 1]
	bobSizes = [2, 2]
	print(f"Input: aliceSizes={aliceSizes}, bobSizes={bobSizes}")
	print(f"Output: {solution.fairCandySwap(aliceSizes, bobSizes)}")
	print()

	aliceSizes = [1, 2]
	bobSizes = [2, 3]
	print(f"Input: aliceSizes={aliceSizes}, bobSizes={bobSizes}")
	print(f"Output: {solution.fairCandySwap(aliceSizes, bobSizes)}")
	print()

	aliceSizes = [2]
	bobSizes = [1, 3]
	print(f"Input: aliceSizes={aliceSizes}, bobSizes={bobSizes}")
	print(f"Output: {solution.fairCandySwap(aliceSizes, bobSizes)}")
	