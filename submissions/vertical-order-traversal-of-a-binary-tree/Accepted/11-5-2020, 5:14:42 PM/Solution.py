// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = collections.defaultdict(list)
        def preorder(root, x, y):
            if not root:
                return
            res[x].append((root.val, y))
            preorder(root.left, x - 1, y - 1)
            preorder(root.right, x + 1, y - 1)
        preorder(root, 0, 0)
        res = [i[1] for i in sorted(res.items(), key=lambda x:x[0])]
        return [[i[0] for i in sorted(j, key=lambda x:(-x[1], x[0]))] for j in res]