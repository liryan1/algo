from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq: List[int] = []
        for num in nums:
            # Binary search to find the insertion index of num
            # to maintain subseq in sorted order
            idx = bisect_left(subseq, num)

            # num is greater than any element of subseq
            if idx == len(subseq):
                subseq.append(num)

            # replace the element in subseq with a small, so that larger
            # elements later can be inserted
            else:
                subseq[idx] = num
        return len(subseq)
