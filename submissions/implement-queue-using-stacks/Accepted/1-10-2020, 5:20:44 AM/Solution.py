// https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:
    """
    本题相当于queue由一反一正两个stack并排构成
    push的时候，push到正的stack里面去
    pop的时候，如果反的stack为空则把所有当前元素都划分到反的stack里面去，
    如果反的stack非空则直接从反的stack里面pop出去
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos_stack = []
        self.neg_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pos_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.neg_stack:
            while self.pos_stack:
                elm = self.pos_stack.pop()
                self.neg_stack.append(elm)
        
        return self.neg_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.neg_stack[-1] if self.neg_stack else self.pos_stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.neg_stack and not self.pos_stack
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()