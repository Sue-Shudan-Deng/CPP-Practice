// https://leetcode.com/problems/design-hashset

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 771
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
        
    def _hash(self, key: int) -> int:
        return key % self.keyRange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
        
class Bucket:
    def __init__(self):
        self.set = BSTree()
        
    def insert(self, value: int):
        self.set.root = self.set.insertBST(self.set.root, value)
        
    def delete(self, value: int):
        self.set.root = self.set.deleteBST(self.set.root, value)

    def exists(self, value: int) -> bool:
        return self.set.searchBST(self.set.root, value) is not None
    
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
class BSTree:
    def __init__(self):
        self.root = None
        
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        
    def insertBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertBST(root.left, val)
        elif val == root.val:
            return root  # 这里注意！！！！！！！非常巧妙，有效规避了key相同的情况
        else:
            root.right = self.insertBST(root.right, val)
        return root
        
    def successor(self, root: TreeNode) -> TreeNode:
        root = root.right
        while root.left:
            root = root.left
        return root
        
    def deleteBST(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        if root.val == key:
            if not root.left:
                root.right = self.deleteBST(root.right, key)
            elif not root.right:
                root.left = self.deleteBST(root.left, key)
            else:
                succ = self.successor(root)
                root.val = succ.val
                root.right = self.deleteBST(root.right, succ.val)
            return root
        
        if val < root.val:
            root.left = self.deleteBST(root.left, val)
        else:
            root.right = self.deleteBST(root.right, val)
        return root

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)