// https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        merge sort (top down)
        1. split  2. sort l1 and l2  3. merge l1 and l2  
        """
        if not head or not head.next:
            return head
        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2
        # split 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        head2 = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(head2)
        return merge(l1, l2)
        """
#         merge sort (botton up)
#         这里最难的是split函数的定义和for loop
#         """
        
#         def split(head, n):
#             """
#             split the head with the first n element and the rest
#             return the rest
#             """
#             while head and n:
#                 head = head->next
#                 n -= 1
#             rest = head if head.next else None
#             if head:
#                 head.next = None
#             return rest
        
#         def merge(l1, l2):
#             if not l1:
#                 return l2
#             if not l2:
#                 return l1
#             if l1.val < l2.val:
#                 l1.next = merge(l1.next, l2)
#                 return l1
#             else:
#                 l2.next = merge(l1, l2.next)
#                 return l2