// https://leetcode.com/problems/lru-cache

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = [0] * capacity
        self.LRU = [0] * capacity
        self.mapping = [None] * capacity
        self.counter = 0
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            idx = self.mapping.index(key)
            self.counter += 1
            self.LRU[idx] = self.counter
            return self.cache[idx]
        except:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        try: 
            idx = self.mapping.index(key)
        except:
            idx = self.LRU.index(sorted(self.LRU)[0])
        self.counter += 1
        self.LRU[idx] = self.counter
        self.mapping[idx] = key
        self.cache[idx] = value
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)