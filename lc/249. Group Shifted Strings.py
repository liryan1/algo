class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        groups: dict[tuple, list[str]] = {}
        for s in strings:
            key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
            groups.setdefault(key, []).append(s)
        return list(groups.values())


s = Solution()
print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
