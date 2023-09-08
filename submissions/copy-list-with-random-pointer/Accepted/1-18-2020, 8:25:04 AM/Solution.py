// https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visited = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Recursion
        """
        if not head:
            return head
        if self.visited.get(head):
            return self.visited[head]
        node = Node(head.val, None, None)
        self.visited[head] = node # 注意: 这里需要先hash，再next和random，否则后面递归的时候也可能访问该结点
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
        