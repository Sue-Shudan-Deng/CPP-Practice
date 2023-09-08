// https://leetcode.com/problems/binary-tree-maximum-path-sum

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
    int ans;
    int dfs(TreeNode* root) {
        // return only one child
        if (!root) {
            return 0;
        }
        if (!root->left && !root->right) {
            return root->val;
        }
        int l = max(0, dfs(root->left));
        int r = max(0, dfs(root->right));
        ans = max(ans, l + r + root->val);
        return root->val + max(l, r);
    }
    
public:
    int maxPathSum(TreeNode* root) {
        int res = dfs(root);
        return ans;
    }
};