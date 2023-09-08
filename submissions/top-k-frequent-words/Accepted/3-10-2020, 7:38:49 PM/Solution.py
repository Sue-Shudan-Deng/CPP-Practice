// https://leetcode.com/problems/top-k-frequent-words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        words = list(cnt.keys())
        words.sort(key = lambda word: (-cnt[word], word))
        return words[:k]