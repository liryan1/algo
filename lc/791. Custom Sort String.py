class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """Bucket sort"""
        chars = [0] * 26
        for ch in s:
            chars[ord(ch) - 97] += 1

        result = []
        # Add all chars in order to the new string
        for ch in order:
            char_idx = ord(ch) - 97
            result.append(ch * chars[char_idx])
            chars[char_idx] = 0

        for i in range(len(chars)):
            if chars[i]:
                result.append(chars[i] * chr(i + 97))

        return "".join(result)
