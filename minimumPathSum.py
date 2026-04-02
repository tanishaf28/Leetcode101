#  Problem (Short)
# Given a grid of non-negative numbers, find a path from top-left to bottom-right
# such that the sum of numbers along the path is minimized.
# You can only move RIGHT or DOWN.

#  Approach (Dynamic Programming - In-place)
# - Each cell represents the minimum cost to reach that cell.
# - From any cell (i, j), you can come from:
#     • top    → (i-1, j)
#     • left   → (i, j-1)
# - So, update each cell as:
#     grid[i][j] += min(top, left)

#  Edge Handling:
# - First row → can only come from LEFT
# - First column → can only come from TOP
# - Start cell (0,0) remains unchanged

# ⏱ Complexity:
# - Time: O(m * n)
# - Space: O(1) (modifying grid in-place)

class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]
