// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
// preorder recursion
private:
    void reserialize(TreeNode* root, string& s) {
        if (!root) {
            s += "None,";
            return;
        }
        s += (to_string(root->val) + ",");
        reserialize(root->left, s);
        reserialize(root->right, s);
    }
    
    TreeNode* redeserialize(deque<string>& q) {
        string s = q.front();
        q.pop_front();
        if (s == "None") {
           return nullptr;
        }
        
        TreeNode* root = new TreeNode(stoi(s));
        root->left = redeserialize(q);
        root->right = redeserialize(q);
        return root;
    }
    
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s = "";
        reserialize(root, s);
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        deque<string> q;
        stringstream ss(data);
        string token;
        while (getline(ss, token, ',')) {
            q.push_back(token);
        }
        // for (auto i: q) cout << i << " ";
        // cout << endl;
        return redeserialize(q);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));