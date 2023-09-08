// https://leetcode.com/problems/lru-cache

import numpy as np
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
        try:
            index = self.mapping[key]
            self.LRU[index] += 1
            return self.cache[index]
        except:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = np.argmin(self.LRU)
        try:
            ori_key = {v:k for k, v in self.mapping.items()}[index]
            del self.mapping[ori_key]
        except:
            pass
        self.LRU[index] += 1
        self.mapping[key] = index
        self.cache[index] = value
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)