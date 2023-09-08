// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        双指针, 最直接的版本
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
            if tail:
                tail.next = ListNode(first.val)
                tail = tail.next
            else:
                tail = ListNode(first.val)
                head = tail
            first = first.next
        
        while not first and second:
            if tail:
                tail.next = ListNode(second.val)
                tail = tail.next
            else:
                tail = ListNode(second.val)
                head = tail
            second = second.next
            
        return head
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        双指针，改进版本
        """
        prehead = ListNode(-1)  # dummy head
        tail = prehead
        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        return prehead.next