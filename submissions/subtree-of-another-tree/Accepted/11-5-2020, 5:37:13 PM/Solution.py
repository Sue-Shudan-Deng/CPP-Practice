// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        方法一：判断是否equal
        """
        return s and (self.equals(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
    
    def equals(self, s: TreeNode, t: TreeNode) -> bool:
        """
        一定要记住标准写法！！！！
        """
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        return s.val == t.val and self.equals(s.left, t.left) \
            and self.equals(s.right, t.right)