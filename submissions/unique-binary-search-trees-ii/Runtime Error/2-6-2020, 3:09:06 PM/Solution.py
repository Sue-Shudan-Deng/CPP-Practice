// https://leetcode.com/problems/unique-binary-search-trees-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate_trees(start, end):
            """
            先生成左右子树，然后把左右子树集合中的每一棵树
            与根结点合并，更新树集合
            """
            if start > end:
                return [None]
            
            alltrees = []
            for i in range(start, end+1):
                left_trees = generate_trees(start, i)
                right_trees = generate_trees(i+1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        alltrees.append(root)
                        
            return alltrees
        
        return generate_trees(1, n) if n else []