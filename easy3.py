"""
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

Constraints:
The given dates are valid dates between the years 1971 and 2100.
 """


class Solution(object):
	def dayOfTheWeek(self, day, month, year):
		"""
		:type day: int
		:type month: int
		:type year: int
		:rtype: str
		"""
		import datetime
		day_of_week = datetime.datetime(year=year, month=month, day=day).isoweekday()
		if day_of_week == 1:
			return "Monday"
		elif day_of_week == 2:
			return "Tuesday"
		elif day_of_week == 3:
			return "Wednesday"
		elif day_of_week == 4:
			return "Thursday"
		elif day_of_week == 5:
			return "Friday"
		elif day_of_week == 6:
			return "Saturday"
		elif day_of_week == 7:
			return "Sunday"
		else:
			return "Invalid day"


if __name__ == '__main__':
	solution = Solution()
	
	day = 31
	month = 8
	year = 2019
	print(f"Input: day={day}, month={month}, year={year}")
	print("Output: " + solution.dayOfTheWeek(6, 3, 1995))
	print()
	
	day = 18
	month = 7
	year = 1999
	print(f"Input: day={day}, month={month}, year={year}")
	print("Output: " + solution.dayOfTheWeek(day, month, year))
	print()
	
	day = 15
	month = 8
	year = 1993
	print(f"Input: day={day}, month={month}, year={year}")
	print("Output: " + solution.dayOfTheWeek(day, month, year))
