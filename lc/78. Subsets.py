class Solution:
    def backtrack(self, nums, idx, curr, sets) -> None:
        sets.append(curr)
        for i in range(idx, len(nums)):
            self.backtrack(nums, i + 1, curr + [nums[i]], sets)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        sets: list[list[int]] = []
        self.backtrack(nums, 0, [], sets)
        return sets


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
