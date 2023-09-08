// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret, level = [], 0
        queue = deque([root])
        while queue:
            ret.append([])
            level_length = len(queue)
            for i in range(level_length):
                root = queue.popleft()
                ret[level].append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            level += 1
        return ret