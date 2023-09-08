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

// Recursion 最好的写法

// class Solution {
//     private:
//         void preorderTraversal(TreeNode* root, vector<int> &ret) {
//             if (!root) return;
//             ret.push_back(root->val);
//             preorderTraversal(root->left, ret);
//             preorderTraversal(root->right, ret);        
//         }

//     public:
//         vector<int> preorderTraversal(TreeNode* root) {
//             vector<int> ret;
//             preorderTraversal(root, ret);
//             return ret;
//         }
// };

// Recursion 常规的写法
    
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

// Interation 常规写法

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (!root) {
            return ret;
        } else {
            std::stack<TreeNode*> s;
            s.push(root);
            TreeNode* cur;
            while (!s.empty()) {
                curr = s.top();
                s.pop();
                ret.push_back(cur->val);
                if (cur->right) s.push(cur->right);
                if (cur->left) s.push(cur->left);
            }
            return ret;
        }
    }
};


