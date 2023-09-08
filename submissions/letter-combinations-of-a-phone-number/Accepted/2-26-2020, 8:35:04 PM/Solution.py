// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
        
        def bt(curr = "", nxt = digits):
            if nxt == "":
                ans.append(curr)
                return
            else:
                for i in phone[nxt[0]]:
                    bt(curr + i, nxt[1:])
        bt()
        return ans if digits != "" else [] 