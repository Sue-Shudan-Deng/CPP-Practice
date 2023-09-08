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
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        # phase two: entrance
        first, second = head, slow
        while first != second:
            first = first.next
            second = second.next
        return first