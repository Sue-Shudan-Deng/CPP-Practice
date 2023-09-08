// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

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
    map<int, int> m;
    int size = 0;
    TreeNode* buildNode(int left, int right, deque<int>& preorder) {
        if (left > right) return nullptr;
        int cur = preorder.front();
        preorder.pop_front();
        int root_index = m.at(cur);
        TreeNode* root = new TreeNode(cur);
        
        root->left = buildNode(left, root_index-1, preorder);
        root->right = buildNode(root_index+1, right, preorder);
        return root;
    }
    
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        size = inorder.size();
        for (int i=0; i < size; ++i) {
            m.emplace(inorder.at(i), i);
        }
        deque<int> q(preorder.begin(), preorder.end());
        return buildNode(0, size-1, q);
    }
};