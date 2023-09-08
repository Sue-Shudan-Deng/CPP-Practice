// https://leetcode.com/problems/sentence-similarity-ii

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        if len(pairs) == 0:
            return words1 == words2
        word_set = set()
        for w1, w2 in pairs:
            word_set.add(w1)
            word_set.add(w2)
            
        parent = collections.defaultdict(str)
        size = collections.defaultdict(str)
        n = len(words1)
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return parent[node]
        
        for u, v in pairs:
            if not parent[u]:
                parent[u] = u
            if not parent[v]:
                parent[v] = v
            pu, pv = find(u), find(v)
            if pu == pv:
                continue
            if size[pu] > size[pv]:
                pu, pv = pv, pu
            parent[pu] = pv
            size[pv] += size[pu]
            
        for i in range(n):
            w1, w2 = words1[i], words2[i]
            if not find(w1) == find(w2):
                return False
        return True
            