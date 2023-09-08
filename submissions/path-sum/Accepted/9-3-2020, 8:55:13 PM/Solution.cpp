// https://leetcode.com/problems/path-sum

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
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root) return false;
        stack<pair<TreeNode*, int>> s;
        s.emplace(root, sum);
        while (!s.empty()) {
            auto [cur, summ] = s.top();
            s.pop();
            summ -= cur->val;
            if (!cur->left && !cur->right && summ == 0) return true;
            if (cur->right) s.emplace(cur->right, summ);
            if (cur->left) s.emplace(cur->left, summ);
        }
        return false;
    }
};