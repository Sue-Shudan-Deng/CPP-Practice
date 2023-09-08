// https://leetcode.com/problems/copy-list-with-random-pointer

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
    
private:
    map<Node*, Node*> visited;    
    
public:
    Node* copyRandomList(Node* head) {
        if (!head) {
            return head;
        }
        if (visited.count(head)) {
            return visited[head];
        }
        
        Node* cur = new Node(head->val);
        visited[head] = cur;
        cur->next = copyRandomList(head->next);
        cur->random = copyRandomList(head->random);
        return visited[head];
    }
};