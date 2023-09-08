// https://leetcode.com/problems/clone-graph

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
    
private:
    map<Node*, Node*> visited;
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        if (visited.find(node) != visited.end()) {
            return (*visited.find(node)).second;
        }
        Node* cloned = new Node(node->val);
        visited.emplace(node, cloned);
        for (auto i : node->neighbors) {
            if (visited.find(node) != visited.end()) {
                cloned->neighbors.push_back(cloneGraph(i));   
            }
        }
        return cloned;
    }
};