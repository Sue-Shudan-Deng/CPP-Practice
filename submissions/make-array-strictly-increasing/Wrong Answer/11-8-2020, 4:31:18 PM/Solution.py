// https://leetcode.com/problems/make-array-strictly-increasing

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(list(set(arr2)))
        n1, n2 = len(arr1), len(arr2)
        keep = [float("inf") for _ in range(n1)]
        swap = [[float("inf") for _ in range(n2)] for _ in range(n1)]
        a, b = arr1, arr2
        
        keep[0] = 0
        swap[0] = [1 for _ in range(n2)]
        
        for i in range(1, n1):
            min_keep, min_swap = float("inf"), float("inf") 
            for j in range(n2):
                # case 1: a[i] > a[i-1]
                if a[i] > a[i-1]:
                    keep[i] = keep[i-1]
                # case 2: b[j] > a[i-1]
                if b[j] > a[i-1]:
                    swap[i][j] = keep[i-1] + 1
                # case 3: a[i] > b[j]
                if a[i] > b[j]:
                    # keep[i] = min([swap[i-1][k] for k in range(j)])
                    min_keep = min(min_keep, swap[i-1][j])
                    keep[i] = min(keep[i], min_keep)
                # case 4: b[j] > b[k]
                if j > 0:
                    # swap[i][j] = min(swap[i-1][k] for k in range(j-1))
                    min_swap = min(min_swap, swap[i-1][j-1] + 1)
                    swap[i][j] = min(swap[i][j], min_swap)
                    
        ans = min(min(swap[-1]), keep[-1])
        return ans if ans != float("inf") else -1
                
                        
                    
        