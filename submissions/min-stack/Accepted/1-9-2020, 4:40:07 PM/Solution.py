// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minval = float("inf")
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.minval:
            self.minval = x

    def updatemin(self):
        newmin = float("inf")
        for item in self.stack:
            if item < newmin:
                newmin = item
        self.minval = newmin
        
    def pop(self) -> None:
        if self.stack:
            item = self.stack.pop()
            if item == self.minval:
                self.updatemin()
            return item 

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minval
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()