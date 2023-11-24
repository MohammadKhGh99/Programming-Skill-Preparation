"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

Constraints:
1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
"""
import re


class Solution(object):
	def mostCommonWord(self, paragraph, banned):
		"""
		:type paragraph: str
		:type banned: List[str]
		:rtype: str
		"""
		# split the paragraph where there is no "word" and put each word in the list
		paragraph_lst = re.split(r"\W", paragraph.lower())
		appearance_count = {}
		for word in paragraph_lst:
			if word != "" and word not in banned:
				if word not in appearance_count:
					appearance_count[word] = 1
				else:
					appearance_count[word] += 1
		# take the key that have the maximum value
		return max(appearance_count.keys(), key=lambda key: appearance_count[key])
		

if __name__ == '__main__':
	solution = Solution()
	
	paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
	banned = ["hit"]
	print(f"Input: paragraph={paragraph}, banned={banned}")
	print(f"Output: {solution.mostCommonWord(paragraph, banned)}")
	print()

	paragraph = "a."
	banned = []
	print(f"Input: paragraph={paragraph}, banned={banned}")
	print(f"Output: {solution.mostCommonWord(paragraph, banned)}")
