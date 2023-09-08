// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        双指针的想法太巧妙
        """
        ptrA, ptrB = headA, headB
        firstA, firstB = True, True
        while ptrA != ptrB:
            if firstA and not ptrA.next:
                ptrA = headB
                firstA = False
            else:
                ptrA = ptrA.next
            
            if firstB and not ptrB.next:
                ptrB = headA
                firstB = False
            else:
                ptrB = ptrB.next
        
        if not ptrA:
            return None
        return ptrA
        