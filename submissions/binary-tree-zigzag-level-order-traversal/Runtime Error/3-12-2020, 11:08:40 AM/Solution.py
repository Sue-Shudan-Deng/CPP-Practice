// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lvl, res, queue = 0, [], collections.deque([root])
        while queue:
            if len(res) < lvl + 1:
                res.append([])
            for _ in range(len(queue)):
                root = queue.popleft()
                res[lvl].append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            if lvl % 2 == 1:
                res[lvl] = res[lvl][::-1]
            lvl += 1
        return res