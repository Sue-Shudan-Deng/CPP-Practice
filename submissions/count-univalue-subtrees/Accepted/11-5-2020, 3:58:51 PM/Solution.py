// https://leetcode.com/problems/count-univalue-subtrees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        self.count = 0
        def isUnival(root):
            if not root:
                return True
            flag = True
            if root.left:
                flag &= (isUnival(root.left) and root.left.val == root.val)
            if root.right:
                flag &= (isUnival(root.right) and root.right.val == root.val)
            if flag:
                self.count += 1
            return flag
        isUnival(root)
        return self.count