// https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        方法一：最朴素的解法
        """
        def inorder(root: TreeNode) -> List[int]:
            if not root:
                return []
            res, stack = [], []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                res.append(root.val)
                root = root.right
            return res
        
        def find_two_swapped(nums: List[int]) -> (int, int):
            """
            中序遍历的BST必然满足"前一个＜后一个"
            """
            x, y = -1, -1
            for i in range(len(nums)):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        # second occurance, break
                        break
            return x, y
        
        def recover(node: TreeNode, cnt: int):
            if not node:
                return 
            if node.val == x:
                node.val = y
                cnt -= 1
            elif node.val == y:
                node.val = x
                cnt -= 1
            if cnt == 0:
                return
            recover(node.left, cnt)
            recover(node.right, cnt)
            
        nums = inorder(root)
        x, y = find_two_swapped(nums)
        recover(root, 2)
            
            
            
            
            
                
        