from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wanted = Counter(t)
        curr: Counter[str] = Counter()
        sub = ""
        lo = hi = 0
        while hi < len(s):
            curr[s[hi]] += 1
            while all(wanted[k] <= curr[k] for k in wanted):
                if not sub or hi - lo < len(sub):
                    end = hi + 1
                    sub = s[lo:end]
                curr[s[lo]] -= 1
                curr = +curr
                lo += 1
            hi += 1

        return sub


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("ADOBECODEBANC", "AC"))
print(s.minWindow("ADOBECODEBANC", "A"))
print(s.minWindow("ABC", "D"))
