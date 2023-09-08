// https://leetcode.com/problems/two-sum-iii-data-structure-design

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if not self.m.get(number, 0):
            self.m[number] = 0
        self.m[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.m.keys():
            if value - n in self.m:
                if n == value:
                    if self.m[n] >= 2:
                        return True
                else:
                    return True

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)