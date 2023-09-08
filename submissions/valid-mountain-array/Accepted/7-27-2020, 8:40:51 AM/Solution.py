// https://leetcode.com/problems/valid-mountain-array

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return False
        flag = False
        for i in range(1, len(A) - 1):
            if not flag:
                if not (A[i] > A[i-1] and A[i+1] > A[i]):
                    if A[i] > A[i-1] and A[i] > A[i+1]:
                        flag = True
                    else:
                        return False
            else:
                if not (A[i-1] > A[i] and A[i] > A[i+1]):
                    return False
        return True if flag else False
                