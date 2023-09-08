// https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 == 1:
                if A[j] % 2 == 0:
                    A[i], A[j] = A[j], A[i]
                j -= 1
            i += 1
            
        return A