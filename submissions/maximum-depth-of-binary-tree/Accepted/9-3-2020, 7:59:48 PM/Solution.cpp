// https://leetcode.com/problems/maximum-depth-of-binary-tree

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
// class Solution {
// public:
//     int maxDepth(TreeNode* root) {
//         if (!root) return 0;
//         return max(maxDepth(root->left), maxDepth(root->right)) + 1;
//     }
// };

class Solution {
public:
    int maxDepth(TreeNode* root) {
        int ret = 0, level = 1;
        if (!root) return ret;
        stack<pair<TreeNode*, int>> s;
        s.emplace(root, level);
        while (!s.empty()) {
            auto [cur, level] = s.top();
            s.pop();
            ret = max(ret, level);
            if (cur->right) s.emplace(cur->right, level + 1);
            if (cur->left) s.emplace(cur->left, level + 1);
        }
        return ret;
    }
};