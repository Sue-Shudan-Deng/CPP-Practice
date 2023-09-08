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
    def hasPathSum(self, root: TreeNode, summ: int) -> bool:
        if not root:
            return False
        queue = deque([(root, summ)])
        while queue:
            curr, summ = queue.popleft()
            summ -= curr.val
            if not curr.left and not curr.right and summ == 0:
                return True
            if curr.left:
                queue.append((curr.left, summ))
            if curr.right:
                queue.append((curr.right, summ))
        return False