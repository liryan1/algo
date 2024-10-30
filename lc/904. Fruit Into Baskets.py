from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Sliding window - the window never decreases.
        If the length of the current window <= 2, the window increases,
        since we are picking more of the same fruit.
        If the length of the current window is greater than 2,
        the window does not increase. j - i + 1 is always the max window.
        """
        count: dict[int, int] = {}
        i = 0  # left window
        for j, v in enumerate(fruits):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
        return j - i + 1
