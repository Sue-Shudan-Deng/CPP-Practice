// https://leetcode.com/problems/binary-tree-preorder-traversal

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

// Recursion

class Solution {
    
private:
    vector<int> preorderTraversal(TreeNode* root, vector<int> &ret) {
        if (!root) return ret;
        ret.push_back(root->val);
        preorderTraversal(root->right, ret);
        preorderTraversal(root->left, ret);        
    }
    
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        preorderTraversal(root, ret);
        return ret;
}
    
    
// class Solution {
    
// public:
//     vector<int> preorderTraversal(TreeNode* root) {
//         vector<int> ret;
//         if (root) {
//             return ret;
//         } else {
//             ret.push_back(root->val);
//             vector<int> v1 = preorderTraversal(root->left);
//             vector<int> v2 = preorderTraversal(root->right);
//             ret.insert(ret.end(), v1.begin(), v1.end());
//             ret.insert(ret.end(), v2.begin(), v2.end());
//             return ret;
//         }
//     }
// };

// Interation

// class Solution {
// public:
//     vector<int> preorderTraversal(TreeNode* root) {
//         vector<int> ret;
//         if (!root) {
//             return ret;
//         } else {
//             std::stack<TreeNode*> stack;
//             stack.push(root);
//             while (!stack.empty()) {
//                 TreeNode* curr = stack.top();
//                 stack.pop();
//                 ret.push_back(curr->val);
//                 if (curr->right) stack.push(curr->right);
//                 if (curr->left) stack.push(curr->left);
//             }
//             return ret;
//         }
//     }
// };


