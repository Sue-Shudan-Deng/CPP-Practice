// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         """
#         方法一: 用hash table
#         """
#         nodes = set()
#         while head:
#             if not head in nodes:
#                 nodes.add(head)
#             else:
#                 return True
#             head = head.next
#         return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        方法二: 用快慢指针
        慢指针每次走一格，快指针每次走两格
        只要有环，快指针一定会追上慢指针
        """
        if not head:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False