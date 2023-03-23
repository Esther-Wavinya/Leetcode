# Problem:

# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2]1] has each integer's value set to its depth.
# Return the sum of each integer in nsestedList multiplied by its depth

# Example 1:
# nestedList = [[1,1],2,[1,1]]
# depth =        2  2  2 2  2
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10.
# Explanation: four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10

# Example 2:
# nestedList = [1,[4,[6]]]
# depth =       1  2  3
# Input: nestedList = [1,[4,[6]]]
# Output: 27.
# Explanation: one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27

# Example 3:
# Input: nestedList = [0]
# Output: 0

# Constraints:
# 1 <= nestedList.length <=50
# The values of the integers in the nested list is in the range [-100, 100]
# The maximum depth of any integer is less than or equal to 50


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

nestedList = [1, [4, [6]]]


class Solution:
    def depthSum(self, nestedList: list[NestedInteger]) -> int:
        # DFS recursively - nestedList = [1,[4,[6]]]
        # at the beginning initialize the total is zero, and start processing every single item in the nestedList and the first one is 1 and assign depth as 1 and after that I will check if this is an integer. If this is an integer I will just calculate the number by mulplying 1 by 1 and add it to the total. For the next layer I am going to check if this item is a list. If this is a list, I am going to recursively run Depth First Serch(DFS) on the list. So the total in this case should be after I get the list and run the DFS on the list but the depth should be plus 1 because everything in this list compared to 4 and 6, atleast should have a depth of 2 beginning from 4 so then when I run the depth search I want to make sure the depth needs to add one and then after adding everything together and recursively, I want to return the total number.

        # list is the list inside of the nestedList, it could be an integer.
        def dfs(list, depth):
            total = 0
            for n in list:  # For every item in the list
                if n.isInteger():  # to check if it is an integer
                    total += n.getInteger()*depth  # if it is an integer, calculate the total
                else:
                    # if it is not an integer, it is a list. if it is a list, run dfs on the list and depth more layer.
                    total += dfs(n.getList(), depth+1)
            return total
        return dfs(nestedList, 1)
