class Solution:
    def searchRange(self, nums, target) -> list[int]:
        n = len(nums)
        positions = [-1, -1]

        # Find left position
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
                positions[0] = mid
                break

            if nums[mid] < target:  # if equal we want to look left
                lo = mid + 1
            else:
                hi = mid

        # Find right position
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target and (mid == n - 1 or nums[mid + 1] > target):
                positions[1] = mid
                break

            if nums[mid] <= target:  # if equal, we want to look right
                lo = mid + 1
            else:
                hi = mid

        return positions
