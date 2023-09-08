// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        首先坚信双指针是可以用的，其次把临时变量一定要存起来
        """
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
    
# 递归(非常巧妙！！！)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None # 指向天上
        return p
        
        