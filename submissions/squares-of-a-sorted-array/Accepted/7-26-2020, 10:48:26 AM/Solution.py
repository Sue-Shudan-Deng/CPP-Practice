// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0 
        while i < len(A) and A[i] < 0:
            i += 1
        j = i
        i = j - 1
        
        ans = []
        while i >= 0 and j < len(A):
            if A[i] ** 2 < A[j] ** 2:
                ans.append(A[i] ** 2)
                i -= 1
            else:
                ans.append(A[j] ** 2)
                j += 1
        
        while i >= 0:
            ans.append(A[i] ** 2)
            i -= 1
            
        while j < len(A):
            ans.append(A[j] ** 2)
            j += 1
        
        return ans