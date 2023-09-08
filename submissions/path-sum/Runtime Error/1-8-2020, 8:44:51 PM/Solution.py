// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion:
# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root: 
#             return False
#         sum -= root.val
#         if not root.left and not root.right:
#             return sum == 0
#         else:
#             return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
# Iteration:
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        queue = deque([(root, sum)])
        while queue:
            curr, sum = queue.popleft()
            sum -= curr.val
            if not curr.left and not curr.right and sum == 0:
                return True
            if curr.left:
                queue.append((curr.left, sum))
            if curr.right:
                queue.append((curr.right, sum))
        return False