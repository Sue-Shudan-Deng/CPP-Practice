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
        if not root:
            return []
        lvl, res, queue = 0, [], collections.deque([root])
        while queue:
            if len(res) < lvl + 1:
                res.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                res[lvl].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvl += 1
        return res