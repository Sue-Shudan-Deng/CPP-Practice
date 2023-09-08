// https://leetcode.com/problems/count-univalue-subtrees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Recursion
        """
        self.cnt = 0
        self.isUnival(root)
        return self.cnt
    
    def isUnival(self, root):
        if not root:
            return False
        # 如果叶结点，自动成为univalue
        if not root.left and not root.right:
            self.cnt += 1
            return True
        flag = True
        if root.left:
            flag &= (self.isUnival(root.left) and root.left.val == root.val)
        if root.right:
            flag &= (self.isUnival(root.right) and root.right.val == root.val)
        if flag:
            self.cnt += 1
        return flag