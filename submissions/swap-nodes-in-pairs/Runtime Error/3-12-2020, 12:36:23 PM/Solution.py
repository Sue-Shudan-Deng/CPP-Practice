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
        Recursion
        """
        fst = head
        snd = head.next
        fst.next = self.swapPairs(snd.next)
        snd.next = fst
        return snd