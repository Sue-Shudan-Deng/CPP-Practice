// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

// BST遍历首选中序遍历
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if (!root) {
            return nullptr;
        }
        Node* first;
        Node* last;
        stack<Node*> s;
        int count = 0;
        while (root || !s.empty()) {
            while (root) {
                s.push(root);
                root = root->left;
            }
            root = s.top();
            s.pop();
            if (count == 0) {
                first = root;
                ++count;
            } else {
                last->right = root;
                root->left = last;
            }
            last = root;
            root = root->right; 
        }
        first->left = last;
        last->right = first;
        return first;
    }
};