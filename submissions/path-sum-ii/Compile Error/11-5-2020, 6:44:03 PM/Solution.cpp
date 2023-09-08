// https://leetcode.com/problems/path-sum-ii

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    
private:
    void dfs(TreeNode* root, int cursum, deque<int> cur, vector<vector<int>>& ans) {
        if (!root) {
            return;
        }
        if (!root->left && !root->right && root->val == cursum) {
            cur.push_back(root->val);
            ans.push_back(vector<int>{tmp(cur.begin(), cur.end())});
            return;
        }
        cur.push_back(root->val);
        dfs(root->left, cursum - root->val, cur, ans);
        dfs(root->right, cursum - root->val, cur, ans);
        cur.pop_front();
    }
    
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> ans;
        deque<int> cur;
        dfs(root, sum, cur, ans);
        return ans;
    }
};