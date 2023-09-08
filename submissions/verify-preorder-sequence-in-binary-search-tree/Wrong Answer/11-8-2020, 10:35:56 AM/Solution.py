// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        q = collections.deque(preorder)
        s = [float("inf")]
        while q:
            cur = q.popleft()
            if cur > s[-1]:
                left = s.pop()
                root = s.pop()
                if not (cur > root and root > left):
                    return False
                s.append(root)
            else:
                s.append(cur)
        return True