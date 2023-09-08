// https://leetcode.com/problems/range-addition

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc
            
            if end + 1 <= length - 1:
                res[end+1] -= inc
        summ = 0
        for i in range(length):
            summ += res[i]
            res[i] = summ
        return res