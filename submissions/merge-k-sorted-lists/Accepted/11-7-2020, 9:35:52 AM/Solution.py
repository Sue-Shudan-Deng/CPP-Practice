// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        in-place
        """
        if not l2:
            return l1
        if not l1:
            return l2
        if l1.val < l2.val:
            l1.next = self.merge2Lists(l1.next, l2)
        else:
            l2.next = self.merge2Lists(l1, l2.next)
        return l1 if l1.val < l2.val else l2
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        本质是button-up mergesort
        """
        size = 1
        while size < len(lists):
            for i in range(0, len(lists) - size, size * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + size])
            size *= 2
        return lists[0] if len(lists) > 0 else None