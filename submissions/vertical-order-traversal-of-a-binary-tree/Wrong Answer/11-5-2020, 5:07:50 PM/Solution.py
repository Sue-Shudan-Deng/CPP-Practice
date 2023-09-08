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
        def preorder(root, x):
            if not root:
                return
            res[x].append(root.val)
            preorder(root.left, x - 1)
            preorder(root.right, x + 1)
        preorder(root, 0)
        return [i[1] for i in sorted(res.items(), key=lambda x:x[0])]