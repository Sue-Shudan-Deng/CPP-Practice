// https://leetcode.com/problems/range-addition

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc
            
            if end + 1 <= length - 1:
                res[end+1] -= inc
        sum = 0
        for i in range(length):
            sum += res[i]
            res[i] = sum
        return res
        
        
        
        