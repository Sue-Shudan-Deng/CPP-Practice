// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def helper(root, level = 0):
            if root:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(root.val)
                helper(root.left, level + 1)
                helper(root.right, level + 1)
            return res
        return helper(root)
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, level = [], 0
        queue = collections.deque([root])
        while queue:
            if len(res) < level + 1:
                res.append([])
            for _ in range(len(queue)):
                root = queue.popleft()
                res[level].append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            level += 1
        return res