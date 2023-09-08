// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Bottom-up RECURSION:
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         else:
#             return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
# Top-down ITERATION (pre-order):
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            answer = 0
            stack = [(root, 1)]
            while stack:
                curr, depth = stack.pop()
                answer = max(answer, depth)
                if curr.right:
                    stack.append((curr.right, depth + 1))
                if curr.left:
                    stack.append((curr.left, depth + 1))
            return answer