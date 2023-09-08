// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        双指针
        """
        first = l1
        second = l2
        tail = None
        head = None
        
        while first and second:
            if first.val <= second.val:
                if tail:
                    tail.next = ListNode(first.val)
                    tail = tail.next
                else:
                    tail = ListNode(first.val)
                    head = tail
                first = first.next
            else:
                if tail:
                    tail.next = ListNode(second.val)
                    tail = tail.next
                else:
                    tail = ListNode(second.val)
                    head = tail
                second = second.next
        
        while not second and first:
            tail.next = ListNode(first.val)
            tail = tail.next
            first = first.next
        
        while not first and second:
            tail.next = ListNode(second.val)
            tail = tail.next
            second = second.next
            
        return head