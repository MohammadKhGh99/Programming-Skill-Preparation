from typing import List


# 1 - Suppose you have a grid of n x m cells, where each cell is either empty or contains a rock.
#     You're given a starting position in the grid (x,y), and you want to reach a target position (tx,ty),
#     but you can only move in four directions (up, down, left, right) and you can only move through empty cells.
#     You're also given a limited number of moves k that you can make. Write a program to determine if it's possible to
#     reach the target position from the starting position within k moves.
#     Example:
#     n = 3, m = 3
#     grid = [[0, 0, 0],
#             [1, 1, 0],
#             [0, 0, 0]]
#     start = (0, 0)
#     target = (2, 2)
#     k = 6
#     Output: true
def can_reach_target(cur_pos: tuple[int, int], grid: List[List[int]], start: tuple[int, int], target: tuple[int, int], k: int):
	# we reach the target
	if cur_pos == target:
		return True
	# we didn't reach the target ,but we reach our maximum moves
	elif k == 0:
		return False
	
	# down - (1, 0)
	# up - (-1, 0)
	# right - (0, 1)
	# left - (0, -1)
	directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	# iterate over all the options in each cell
	for direction in directions:
		# check the chosen option if it is not going outside the borders or if there is a rock in the new position
		temp_pos = cur_pos[0] + direction[0], cur_pos[1] + direction[1]
		if temp_pos[0] < 0 or temp_pos[0] >= len(grid[0]) or temp_pos[1] < 0 or temp_pos[1] >= len(grid) or grid[temp_pos[0]][temp_pos[1]] == 1:
			# if the chosen move is not valid, so continue to the next option
			continue
		else:
			# if the chosen option is valid and we reach the target
			if can_reach_target(temp_pos, grid, start, target, k - 1):
				return True
	
	return False


if __name__ == '__main__':
	grid = [[0, 0, 0], [0, 0, 1], [1, 0, 0]]
	start = (0, 0)
	target = (2, 2)
	k = 6
	print(can_reach_target(start, grid, start, target, k))
