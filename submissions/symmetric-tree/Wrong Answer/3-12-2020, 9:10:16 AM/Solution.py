// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        方法一：Recursion
        """
        return self.isMirror(root, root)
    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        方法二：Iteration
        """
        queue = collections.deque([(root, root)])
        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        return True