// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        龟兔双指针
        """
        # phase one: intersection
        slow, fast = head, head
        if not head or not head.next:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not (fast and fast.next):
            return None
        # phase two: entrance
        first, second = head, slow
        while first != second:
            first = first.next
            second = second.next
        return first