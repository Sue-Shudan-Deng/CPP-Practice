// https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Stack + DFS
        """
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        stack = [(p, q)]
        while stack:
            a, b = stack.pop()
            if not check(a, b):
                return False
            if a and b:
                stack.append((a.right, b.right))
                stack.append((a.left, b.left))
        return True