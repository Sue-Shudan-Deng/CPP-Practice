// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing

class Solution {
    
private:
    int ans;
    void dfs(vector<int>& A, vector<int>& B, int i, int c) {
        if (c >= ans) {
            // no need to continue
            return;
        }
        if (i == A.size()) {
            ans = min(ans, c);
            return;
        } 
        
        if ((i == 0) || (A[i] > A[i-1] && B[i] > B[i-1])) {
            dfs(A, B, i + 1, c); // no need ti switch
        }
        
        if ((i == 0) || (B[i] > A[i-1] && A[i] > B[i-1])) {
            swap(A[i], B[i]);
            dfs(A, B, i + 1, c+1);
            swap(A[i], B[i]);
        }
    }
    
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        ans = INT_MAX;
        dfs(A, B, 0, 0);
        return ans;
    }
};