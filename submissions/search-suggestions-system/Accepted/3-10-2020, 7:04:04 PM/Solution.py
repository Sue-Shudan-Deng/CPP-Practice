// https://leetcode.com/problems/search-suggestions-system

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort in lexicographical order
        products.sort()
        res = []
        for i in range(1, len(searchWord) + 1):
            res.append(list(filter(lambda word: word[:i] == searchWord[:i], products))[:3])
        return res