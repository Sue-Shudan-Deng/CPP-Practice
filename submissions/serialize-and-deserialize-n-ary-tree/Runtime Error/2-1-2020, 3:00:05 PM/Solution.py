// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        stack, output = [root], []
        while stack:
            root = stack.pop()
            length = 0
            for _ in root.children:
                length += 1
            value = str(length) + " " + str(root.val) + " "
            output.append(value)
            for i in range(length-1, -1, -1):
                stack.append(root.children[i])
        return "".join(output)
        

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        return Node("1")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))