// https://leetcode.com/problems/similar-string-groups

class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        A = list(set(A))
        parent = {a:a for a in A}
        size = {a: 0 for a in A}
        n = len(A)
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return
            if size[pu] > size[pv]:
                pu, pv = pv, pu
            parent[pu] = pv
            size[pv] += size[pu]
            
        def is_similar(word1, word2):
            diff, c1, c2 = 0, set(), set()
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                    c1.add(word1[i])
                    c2.add(word2[i])
                if diff > 2: return False
            return True if c1 == c2 else False
        
        if len(A) > len(A[0]):
            # O(N * K^2)
            cache = set(A)
            for a in A:
                for s_word in similar_words(a):
                    if s_word in cache:
                        union(a, s_word)        
        else:
            # O(N^2 * K)
            for i, a in enumerate(A):
                for j in range(i + 1, len(A)):
                    if is_similar(A[i], A[j]):
                        union(A[i], A[j])
                            
        groups = collections.defaultdict(int)
        for word in parent:
            groups[find(word)] += 1
        return len(groups)