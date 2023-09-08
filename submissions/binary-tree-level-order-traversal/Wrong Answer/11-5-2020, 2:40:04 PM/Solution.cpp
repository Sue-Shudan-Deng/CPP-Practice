// https://leetcode.com/problems/binary-tree-level-order-traversal

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
    
// private:
//     void dfs(TreeNode* root, int depth, vector<vector<int>>& ans) {
//         if (!root) {
//             return;
//         }
//         while (ans.size() <= depth) {
//             ans.push_back({});
//         }
//         ans[depth].push_back(root->val);
//         dfs(root->left, depth + 1, ans);
//         dfs(root->right, depth + 1, ans);
//     }
    
// public:
//     // dfs
//     vector<vector<int>> levelOrder(TreeNode* root) {
//         vector<vector<int>> ans;
//         dfs(root, 0, ans);
//         return ans;
//     }
    
//     bfs
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans = {{}};
        if (!root) {
            return ans; 
        }
        int level = 0;
        deque<TreeNode*> q;
        q.push_back(root);
        while (!q.empty()) {
            int size = q.size();
            if (ans.size() < level + 1) {
                ans.push_back({});
            }
            for (auto i = 0; i < size; ++i) {
                TreeNode* root = q.front();
                q.pop_front();
                ans[level].push_back(root->val);
                if (root->left) {
                    q.push_back(root->left);
                }
                if (root->right) {
                    q.push_back(root->right);   
                }
            }
            ++level;
        }
        return ans;
    }
};