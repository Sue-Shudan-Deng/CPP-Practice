// https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def simplify(string: str) -> str:
            local, domain = tuple(string.split('@'))
            if '+' in local:
                local = local.split('+')[0]
            return "".join(local.split('.')) + '@' + domain
        ans = collections.defaultdict(list)
        for e in emails:
            ans[simplify(e)].append(e)
        return len(ans)