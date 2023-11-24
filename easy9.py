"""
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""


class Solution(object):
	def transpose(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		transposed_matrix = []
		for col in range(len(matrix[0])):
			new_row = []
			for row in range(len(matrix)):
				new_row.append(matrix[row][col])
			transposed_matrix.append(new_row)
		
		return transposed_matrix


if __name__ == '__main__':
	solution = Solution()
	
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print(f"Input: matrix={matrix}")
	print(f"Output: {solution.transpose(matrix)}")
	print()
	
	matrix = [[1, 2, 3], [4, 5, 6]]
	print(f"Input: matrix={matrix}")
	print(f"Output: {solution.transpose(matrix)}")
