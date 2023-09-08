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
        return self.traverse(s, t)
    
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
    
    def traverse(self, s: TreeNode, t: TreeNode) -> bool:
        return s != None and (self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))
    
    
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        方法二：先序遍历
        """
        s1 = self.preorder(s)
        s2 = self.preorder(t)
        return all(x in s1.split() for x in s2.split()) and (s2 in s1)
        
    def preorder(self, t: TreeNode) -> str:
        res = ""
        if not t:
            return res
        stack = [t]
        while stack:
            t = stack.pop()
            res += str(t.val) + " "
            if t.right:
                stack.append(t.right)
            else:
                res += "RNone "
            if t.left:
                stack.append(t.left)
            else:
                res += "LNone "
        return res