// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        方法一:用hash table
        """
        nodes = set()
        while head:
            if not head in nodes:
                nodes.add(head)
            else:
                return True
            head = head.next
        return False