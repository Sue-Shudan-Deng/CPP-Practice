// https://leetcode.com/problems/lru-cache

import numpy as np
import time

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = [0] * capacity
        self.LRU = [0] * capacity
        self.mapping = [None] * capacity
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            idx = self.mapping.index(key)
            self.LRU[idx] = time.time()
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
            idx = np.argmin(self.LRU)
        self.LRU[idx] = time.time()
        self.mapping[idx] = key
        self.cache[idx] = value
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)