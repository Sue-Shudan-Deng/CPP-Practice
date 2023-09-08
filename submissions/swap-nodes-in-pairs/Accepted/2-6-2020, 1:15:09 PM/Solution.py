// https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        注: 因为python没有指针，是按引用传递，所以这里的写法非常微妙
        即：最好新赋值几个变量，然后在这些变量上修改，尽量不要直接在原变量上直接改
        """
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second