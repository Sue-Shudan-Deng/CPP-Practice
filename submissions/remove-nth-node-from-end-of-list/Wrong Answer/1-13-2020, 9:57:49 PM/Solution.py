// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        加dummy head是为了让idx算起来更方便，这样n就是n不是n-1
        """
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy 
        for _ in range(n):
            second = second.next
        
        while second.next:
            first = first.next
            second = second.next
            
        first.next = first.next.next
        return head