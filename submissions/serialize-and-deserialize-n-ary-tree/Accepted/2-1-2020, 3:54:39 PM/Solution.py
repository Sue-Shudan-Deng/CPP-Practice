// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def serealizeHelper(root:'Node', sb):
            if not root: 
                return
            sb.append(str(root.val) + ",")
            sb.append(str(len(root.children)) + ",") 
            for child in root.children:
                serealizeHelper(child, sb)
        
        if not root:
            return ""
        sb = []
        serealizeHelper(root, sb)
        print("".join(sb))
        return "".join(sb)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        global i
        i = 0
        def deserializeHelper(s: str) -> 'Node':
            global i
            node = Node(s[i], [])
            i += 1
            count = int(s[i])
            i += 1

            for j in range(count):
                node.children.append(deserializeHelper(s))
            return node
        
        if len(data) is 0:
            return None
        arr = data.split(",")
        return deserializeHelper(arr)
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))