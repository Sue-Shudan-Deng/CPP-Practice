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
    
private:
    void dfs(TreeNode* root, int depth, vector<vector<int>>& ans) {
        if (!root) {
            return;
        }
        while (ans.size() <= depth) {
            ans.push_back({});
        }
        ans[depth].push_back(root->val);
        dfs(root->left, depth + 1, ans);
        dfs(root->right, depth + 1, ans);
    }
    
public:
    // dfs
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        dfs(root, 0, ans);
        return ans;
    }
    
    // bfs
    // vector<vector<int>> levelOrder(TreeNode* root) {
    //     vector<vector<int>> ret;
    //     if (!root) return ret;
    //     queue<TreeNode*> q;
    //     int level, size;
    //     TreeNode* cur;
    //     q.push(root);
    //     while (!q.empty()) {
    //         vector<int> tmp;
    //         ret.push_back(tmp);
    //         size = q.size();
    //         for (int i = 0; i < size; ++i) {
    //             cur = q.front();
    //             q.pop();
    //             ret[level].push_back(cur->val);
    //             if (cur->left) q.push(cur->left);
    //             if (cur->right) q.push(cur->right);
    //         }
    //         ++level;
    //     }
    //     return ret;
    // }
};