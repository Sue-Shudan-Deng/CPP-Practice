// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    
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
    

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        递归，思维也太巧妙了
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2