// https://leetcode.com/problems/find-duplicate-subtrees

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
    vector<TreeNode*> ans;
    map<string, int> m;
    string serialize(TreeNode* root) {
        if (!root) {
            return "#";
        }
        string key = to_string(root->val) + serialize(root->left) + serialize(root->right);
        if (m.count(key) == 0) {
            m[key] = 0;
        }
        ++m[key];
        if (m[key] == 2) {
            ans.push_back(root);
        }
        return key;
    }
    
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        string s = serialize(root);
        return ans;
    }
};