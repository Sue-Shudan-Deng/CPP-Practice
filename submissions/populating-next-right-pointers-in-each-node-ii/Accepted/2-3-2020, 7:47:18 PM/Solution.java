// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
    public Node connect(Node root) {
        Node orig = root;
        while (root != null) {
            Node sentinel = new Node(0), cur = sentinel;
            while (root != null) {
                if (root.left != null) {
                    cur.next = root.left;
                    cur = cur.next;
                }
                if (root.right != null) {
                    cur.next = root.right;
                    cur = cur.next;
                }
                root = root.next;
            }
            root = sentinel.next;
        }
        return orig;
    }
}