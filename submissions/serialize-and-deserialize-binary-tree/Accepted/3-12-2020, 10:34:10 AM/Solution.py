// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string = ""):
            if not root:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        return rserialize(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(preorder):
            if preorder[0] == "None":
                preorder.pop(0)
                return None
            
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            root.left = rdeserialize(preorder)
            root.right = rdeserialize(preorder)
            return root
        
        preorder = data.split(",")
        return rdeserialize(preorder)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))