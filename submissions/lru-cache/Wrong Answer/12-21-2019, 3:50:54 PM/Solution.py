// https://leetcode.com/problems/lru-cache

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = [0] * capacity
        self.LRU = [0] * capacity
        self.mapping = dict()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self.mapping[key]
        self.LRU[index] += 1
        return self.cache[index]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = min(self.LRU)
        self.LRU[index] += 1
        print(index)
        self.mapping[key] = index
        self.cache[index] = value
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)