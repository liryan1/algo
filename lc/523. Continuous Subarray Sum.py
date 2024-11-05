class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainders = {0: -1}  # 0 at index -1 handles len(nums) == 2
        s = 0
        for i in range(len(nums)):
            s = (s + nums[i]) % k
            prev_idx = remainders.get(s)
            if prev_idx is not None:
                if i - prev_idx > 1:
                    return True
            else:
                remainders[s] = i
        return False
