// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree

class Solution {
public:
    void dfs(vector<int>& preorder, int& start, int lower, int upper) {
        if (start >= preorder.size() || preorder[start] < lower || preorder[start] > upper)
            return;
        int val = preorder[start++];
        dfs(preorder, start, lower, val);
        dfs(preorder, start, val, upper);
    }

    bool verifyPreorder(vector<int>& preorder) {
        int start = 0;
        dfs(preorder, start, INT_MIN, INT_MAX);

        return start == preorder.size();
    }  
};