// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion:
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: 
            return sum == 0
        
        leftsum = self.hasPathSum(root.left, sum - root.val)
        rightsum = self.hasPathSum(root.right, sum - root.val)
        
        return leftsum or rightsum

# # Iteration:
# from collections import deque
# class Solution:
#     def hasPathSum(self, root: TreeNode, summ: int) -> bool:
#         if not root:
#             return False
#         queue = deque([(root, summ)])
#         while queue:
#             curr, summ = queue.popleft()
#             summ -= curr.val
#             if not curr.left and not curr.right and summ == 0:
#                 return True
#             if curr.left:
#                 queue.append((curr.left, summ))
#             if curr.right:
#                 queue.append((curr.right, summ))
#         return False