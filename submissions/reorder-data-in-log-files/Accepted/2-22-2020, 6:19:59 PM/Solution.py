// https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        注：这段代码确实写得好
        """
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)
        return sorted(logs, key = f)