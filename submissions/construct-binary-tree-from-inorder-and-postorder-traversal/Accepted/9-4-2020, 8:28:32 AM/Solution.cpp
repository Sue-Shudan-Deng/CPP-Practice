// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

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
    TreeNode* buildNode(int left_index, int right_index, vector<int>& postorder) {
        if (left_index > right_index) return nullptr;
        int cur = postorder.back();
        postorder.pop_back();
        TreeNode* root = new TreeNode(cur);
        int root_index = m.at(cur);
        root->right = buildNode(root_index+1, right_index, postorder);
        root->left = buildNode(left_index, root_index-1, postorder);
        return root;
    }
    
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        size = inorder.size();
        for (int i=0; i < size; ++i) {
            m.emplace(inorder.at(i), i);
        }
        // for (auto &i : m) cout << i.first << " " << i.second << endl;
        return buildNode(0, size-1, postorder);
    }
};