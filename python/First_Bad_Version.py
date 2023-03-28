# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.


# Example 2:
# Input: n = 1, bad = 1
# Output: 1

# Constraints:
# 1 <= bad <= n <= 231 - 1


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# One way to solve this problem is to use a binary search algorithm. We can start by checking the middle version, and based on the result, we can determine whether the first bad version is to the left or right of the middle. We can continue this process of dividing the search space in half until we find the first bad version.
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# The time complexity of this solution is 0(log n) since we are dividing the search space in half at each step of the binary search. We only make a call to the isBadVersion API once for each version, so the number of API calls is also minimized.abs(x)
