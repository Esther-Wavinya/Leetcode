# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# To solve this problem, we can use a breadth-first search (BFS) algorithm. We start by adding the root node to a queue. Then, we loop through the queue, popping out each node one by one, and adding its left and right children (if they exist) to the queue. We keep track of the level we are at and the nodes at that level, adding the nodes to a list that we append to our final result list once we have processed all nodes at that level.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # check if the root node exists, if it does not exist, we return an empty list since there are no nodes to process
        if not root:
            return []
        # create a deque object called 'queue' and add the root node to it
        queue = deque([root])
        # create an empty list called 'result' that we will use to store the nodes' values
        result = []
        # loop through the queue, popping out each node one by one using 'queue.popleft()'
        while queue:
            # get the number of nodes in the current level using 'level_size = len(queue)'
            level_size = len(queue)
            # create an empty list called 'level_nodes' to store the nodes at the current
            level_nodes = []

            for i in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result

# We start by checking if the root node exists. If it does not exist, we return an empty list since there are no nodes to process.

# We create a deque object called queue and add the root node to it. We also create an empty list called result that we will use to store the nodes' values.

# We loop through the queue, popping out each node one by one using queue.popleft(). We get the number of nodes in the current level using level_size = len(queue). We create an empty list called level_nodes to store the nodes at the current level.

# We loop through the current level nodes, adding their values to level_nodes. We also add their left and right children (if they exist) to the queue.

# Once we have processed all nodes at the current level, we append level_nodes to result. We continue this process until we have processed all nodes in the tree.

# Finally, we return result, which contains the level order traversal of the nodes' values.
