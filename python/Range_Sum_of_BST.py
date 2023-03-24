# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
# Given the root of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive). The binary search tree is guaranteed to have unique values.


# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15 or L = 7, R = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10 or L = 6, R = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# Constraints:
# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.


# Can be solved iteratively or recursively.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #    """
        #     :type root: TreeNode
        #     :type low: int
        #     :type high: int
        #     :rtype: int
        #     """
        # check what happens if we are given an empty root. in this case we can't sum anything if we don't have anything, just return zero.
        if not root:
            return 0
            # define variable to store our result
        ans = 0
        # since we are solving iteratively, declare variable stack to store our recursion
        stack = [root]

        while stack:
            node = stack.pop()  # current stack we are working with
            # check whether in the node what we have is in the range that we need to sum up
            if node:  # we may not have node or node can be null so we need to make sure it is non-null
                if low <= node.val <= high:  # if node value lies within the range
                    # add that node value to our ans
                    ans += node.val
                # need to check whether we need to go through the left subtree. From the diagram if our value - node.val is greater than low then that means we are allowed to go into the left subtree. If is less than or small already, there is no point of checking the left subtree because the property of a binary search tree is all values in the left child are going to be less than the current parent node's value
                if low < node.val:  # then we are allowed to go into the left subtree
                    # left subtree
                    stack.append(node.left)
                # same thing for the right
                if node.val < high:  # allowed to go into the right subtree
                    # right sub tree
                    stack.append(node.right)

        return ans

# T: O(N)
# S:O(N)
# Alternatively in the worst case, we need to sum up the entirety of the tree


# Recursive solution
class Solution(object):
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #    """
        #     :type root: TreeNode
        #     :type low: int
        #     :type high: int
        #     :rtype: int
        #     """
        # check what happens if we are given an empty root. in this case we can't sum anything if we don't have anything, just return zero.
        if not root:
            return 0

        self.range_sum = 0

        self.dfs(root, low, high)

        return self.range_sum

    def dfs(self, node, low, high):
        if node:
            if low <= node.val <= high:
                self.range_sum += node.val
                # check for left and right trees
            if low < node.val:
                self.dfs(node, left, low, high)

            if node.val < high:
                self.dfs(node, right, low, high)


# T: O(N)
# S: O(N)
