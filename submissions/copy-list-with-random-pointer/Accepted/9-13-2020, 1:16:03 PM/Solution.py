// https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# class Solution:
#     def __init__(self):
#         # Dictionary which holds old nodes as keys and new nodes as its values.
#         self.visited = {}
        
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         """
#         Recursion
#         """
#         if not head:
#             return head
#         if self.visited.get(head):
#             return self.visited[head]
#         node = Node(head.val, None, None)
#         self.visited[head] = node # 注意: 这里需要先hash，再next和random，否则后面递归的时候也可能访问该结点
#         node.next = self.copyRandomList(head.next)
#         node.random = self.copyRandomList(head.random)
#         return node
    
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Iteration
        """
        if not head:
            return head
        self.visited = {}
        old_node = head
        
        def getnode(node):
            if not node:
                return node
            if not node in self.visited:
                new_node = Node(node.val, None, None)
                self.visited[node] = new_node
            return self.visited[node]
        
        new_node = getnode(old_node)
        while old_node:
            new_node.next = getnode(old_node.next)
            new_node.random = getnode(old_node.random)
            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[head]