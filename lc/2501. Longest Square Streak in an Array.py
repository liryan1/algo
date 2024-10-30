from typing import List, Dict


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        We need to process smaller numbers before larger,
        otherwise we have to back track.
        Keep the existing streak for each number and update
        longest with each iteration.
        """

        nums.sort()
        longest = 0
        desired_to_streak: Dict[int, int] = {}
        for num in nums:
            streak = desired_to_streak.get(num, 0) + 1
            longest = max(longest, streak)
            next = num * num
            desired_to_streak[next] = streak

        return longest if longest > 1 else -1
