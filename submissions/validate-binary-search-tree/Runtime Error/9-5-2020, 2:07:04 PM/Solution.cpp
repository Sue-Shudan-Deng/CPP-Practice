// https://leetcode.com/problems/validate-binary-search-tree

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

// // Iteration, 中序遍历
// class Solution {
// public:
//     bool isValidBST(TreeNode* root) {
//         stack<TreeNode*> s;
//         int last = INT_MIN;
//         int counter = 0;
//         while (root || !s.empty()) {
//             while (root) {
//                 s.push(root);
//                 root = root->left;
//             }
//             root = s.top();
//             s.pop();
//             if (root->val <= last && counter != 0) return false;
//             if (counter == 0) counter++;
//             last = root->val;
//             root = root->right;
//         }
//         return true;
//     }
// };

// Iteration, 先序遍历
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        int lower = INT_MIN, upper = INT_MAX;
        stack<tuple<TreeNode*, int, int>> s;
        s.emplace(root, lower, upper);
        while (!s.empty()) {
            auto [root, lower, upper] = s.top();
            s.pop();
            if (root->val != INT_MIN 
             && root->val != INT_MAX 
             && (root->val <= lower || root->val >= upper)) return false;
            if (root->right) s.emplace(root->right, root->val, upper);
            if (root->left) s.emplace(root->left, lower, root->val);
        }
        return true;
    }
};