// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # A little bit hard
        i = 0
        while i < len(A) and A[i] < 0:
            i += 1
        i, j = i-1, i
        
        arr = []
        while i >= 0 and j < len(A):
            if A[i] ** 2 < A[j] ** 2:
                arr.append(A[i] ** 2)
                i -= 1
            else:
                arr.append(A[j] ** 2)
                j += 1
        
        while i >= 0:
            arr.append(A[i] ** 2)
            i -= 1
        while j < len(A):
            arr.append(A[j] ** 2)
            j += 1
        return arr