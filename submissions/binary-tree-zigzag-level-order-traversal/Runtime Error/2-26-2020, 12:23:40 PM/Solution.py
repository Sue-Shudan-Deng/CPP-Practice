// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        注：这里使用recursion的做法应该是完全不可行的
        必须一次性把下一层的所有结点都装进deque才行
        """
        res, level = [], 0
        queue = collections.deque([root])
        isreverse = False
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
            if isreverse:
                res[level] = res[level][::-1]
            level += 1
            isreverse = not isreverse
        return res