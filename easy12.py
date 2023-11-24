"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		s = list(s)
		# get all the indexes of the vowels in the given string
		vowels_indexes = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
		for i in range(len(vowels_indexes) // 2):
			# switch between vowels to reverse
			s[vowels_indexes[i]], s[vowels_indexes[-(i + 1)]] = s[vowels_indexes[-(i + 1)]], s[vowels_indexes[i]]
		return "".join(s)
		

if __name__ == '__main__':
	solution = Solution()
	
	s = "hello"
	print(f"Input: s = {s}")
	print(f"Output: {solution.reverseVowels(s)}")
	print()
	
	s = "leetcode"
	print(f"Input: s = {s}")
	print(f"Output: {solution.reverseVowels(s)}")
