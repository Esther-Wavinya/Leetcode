# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

#     Integers in each row are sorted in ascending from left to right.
#     Integers in each column are sorted in ascending from top to bottom.

# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     1 <= n, m <= 300
#     -109 <= matrix[i][j] <= 109
#     All the integers in each row are sorted in ascending order.
#     All the integers in each column are sorted in ascending order.
#     -109 <= target <= 109


# One approach to solve this problem is to start from the top-right corner of the matrix and compare the value at that position with the target. If the value is greater than the target, we move one column to the left. If the value is smaller than the target, we move one row down. We repeat this process until we either find the target or reach the end of the matrix.
# The reason why we start from the top-right corner is that this position allows us to eliminate one row or one column at each step, making the search more efficient.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False

# The time complexity of this algorithm is O(m + n), where m is the number of rows and n is the number of columns. This is because at each step, we eliminate one row or one column, and we can do this at most m + n times. Therefore, the overall time complexity is linear in the size of the matrix.
