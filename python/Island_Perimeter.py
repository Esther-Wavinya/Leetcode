# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water. / You are given a map in form of a two dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.


# Example 2:
# Input: grid = [[1]]
# Output: 4

# Example 3:
# Input: grid = [[1,0]]
# Output: 4

# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
#

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # we start by initializing the perimeter to zero
        perimeter = 0
        # then we iterate through each cell in the grid. If the cell is a land cell, we add 4 to the perimeter(since a land cell has 4 sides)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # if it is a land cell
                    perimeter += 4  # add 4 since it is a land cell
                    # Next, we check if the cell above or to the left is also a land cell, if it is, we subtract 2 from the perimeter(since two sides of the current cell are shared with the neighboting cell)
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter

# The time complexity of this algorithm is O(rows x cols), since we need to iterate through each cell in the grid. The space complexity is O(1), since we only need a constant amount of extra space to store the perimeter counter and the row and column indices.


# Alternatively
# To calculate the perimeter of the island, we need to count the number of edges that form the boundary of the island.
# We can do this by iterating through each cell in the grid and checking if it is a land cell (i.e., has a value of 1). If it is a land cell, we can check the cells above, below, to the left, and to the right of it to see if they are also land cells. If they are not land cells, then they must be water cells, and their adjacent edges will form part of the perimeter of the island. We can add the number of adjacent water cells to a perimeter counter for each land cell.
def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check cells above, below, to the left, and to the right
                if i == 0 or grid[i-1][j] == 0:  # top edge
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # bottom edge
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # left edge
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # right edge
                    perimeter += 1

    return perimeter

# The time complexity of this algorithm is O(rows x cols), since we need to iterate through each cell in the grid. The space complexity is O(1), since we only need a constant amount of extra space to store the perimeter counter and the row and column indices.
