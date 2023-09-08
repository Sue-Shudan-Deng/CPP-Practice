// https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        first = copy.deepcopy(head)
        second = copy.deepcopy(head.next)
        
        first.next = self.swapPairs(second.next)
        second.next = first
        return second