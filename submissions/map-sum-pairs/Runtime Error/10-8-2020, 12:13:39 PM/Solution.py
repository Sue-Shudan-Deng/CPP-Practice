// https://leetcode.com/problems/map-sum-pairs

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = {}
        self.sums = {}

    def insert(self, key: str, val: int) -> None:
        inc = val
        if key in self.vals:
            inc -= self.vals[key]
        for i in range(1, len(key) + 1):
            self.sums[key[:i]] = self.sums.get(key[:i], 0) + inc

    def sum(self, prefix: str) -> int:
        return self.sums[prefix]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)