// https://leetcode.com/problems/symmetric-tree

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

// recursion
// class Solution {
//     private:
//         bool isMirror(TreeNode* t1, TreeNode* t2) {
//             if (!t1 && !t2) return true;
//             if (!t1 || !t2) return false;
//             return (t1->val == t2->val) && isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left); 
//         }
//     public:
//         bool isSymmetric(TreeNode* root) {
//             if (!root) return true;
//             return isMirror(root->left, root->right);
//         }
// };

// iteration
class Solution {
    public:
        bool isSymmetric(TreeNode* root) {
            if (!root) return true;
            queue<pair<TreeNode*, TreeNode*>> q;
            q.emplace(root->left, root->right);
            while (!q.empty()) {
                auto [t1, t2] = q.front();
                q.pop();
                if (!t1 && !t2) continue;
                if ((!t1 || !t2) || (t1->val != t2 ->val)) return false;
                q.emplace(t1->left, t2->right);
                q.emplace(t1->right, t2->left);
            }
            return true;
        }
};