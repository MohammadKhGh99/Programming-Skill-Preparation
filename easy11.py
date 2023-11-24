"""
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a
zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".
Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could
represent. You may return the answer in any order.

The hour must not contain a leading zero.
For example, "01:00" is not valid. It should be "1:00".

The minute must consist of two digits and may contain a leading zero.
For example, "10:2" is not valid. It should be "10:02".

Example 1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:
Input: turnedOn = 9
Output: []

Constraints:
0 <= turnedOn <= 10
"""


class Solution(object):
	def readBinaryWatch(self, turnedOn):
		"""
		:type turnedOn: int
		:rtype: List[str]
		"""
		# maximum number of turned on bits is 8, we can't turn on 4 hours in the same time, and we can't turn on 6 minutes at the same time
		if turnedOn in [9, 10]:
			return []
		# there is no turned on bits so there is just one option
		if turnedOn == 0:
			return ["0:00"]
		
		result = []
		for h in range(12):
			# count the set bit of the binary representation of the hours
			h_set_bit = bin(h)[2:].count("1")
			if h_set_bit > turnedOn:
				continue
			for m in range(60):
				# count the set bit of the binary representation of the minutes
				m_set_bit = bin(m)[2:].count("1")
				if h_set_bit + m_set_bit == turnedOn:
					if m >= 10:
						result.append(str(h) + ":" + str(m))
					else:
						result.append(str(h) + ":0" + str(m))
		return result


if __name__ == '__main__':
	solution = Solution()
	
	turnedOn = 1
	print(f"Input: turnedOn = {turnedOn}")
	print(f"Output: {solution.readBinaryWatch(turnedOn)}")
	print()
	
	turnedOn = 9
	print(f"Input: turnedOn = {turnedOn}")
	print(f"Output: {solution.readBinaryWatch(turnedOn)}")
