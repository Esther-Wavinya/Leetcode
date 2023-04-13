# Given an m x n matrix, return all elements of the matrix in spiral order.


# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 10
#     -100 <= matrix[i][j] <= 100

# To solve this problem, we need to traverse the matrix in a spiral order. We can do this by keeping track of the boundaries of the matrix and then iterating through each boundary in a spiral manner.

# Here's the approach we can take:

#     Initialize variables for the top, bottom, left, and right boundaries of the matrix.
#     Initialize an empty result list.
#     While the top boundary is less than or equal to the bottom boundary and the left boundary is less than or equal to the right boundary:
#         Traverse the top row from left to right and append each element to the result list.
#         Increment the top boundary.
#         Traverse the right column from top to bottom and append each element to the result list.
#         Decrement the right boundary.
#         If the top boundary is still less than or equal to the bottom boundary, traverse the bottom row from right to left and append each element to the result list.
#         Decrement the bottom boundary.
#         If the left boundary is still less than or equal to the right boundary, traverse the left column from bottom to top and append each element to the result list.
#         Increment the left boundary.
#     Return the result list.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m-1, 0, n-1
        result = []

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# We first check if the matrix is empty and return an empty list if it is. We then initialize the top, bottom, left, and right boundaries of the matrix, and an empty result list. We then iterate through each boundary in a spiral manner and append each element to the result list. Finally, we return the result list.
