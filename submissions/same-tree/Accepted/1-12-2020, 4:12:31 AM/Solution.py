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
            p, q = stack.pop()
            if not check(p, q):
                return False
            if p and q:
                stack.append((p.right, q.right))
                stack.append((p.left, q.left))
        return True