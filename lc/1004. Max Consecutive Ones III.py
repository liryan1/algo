class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        I, II, III
        Sliding window algorithm. If there are more than k zeros, slide the
        left pointer to the right and remove a zero. The window never shrinks.
        """
        zeros = 0
        left = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

        return i - left + 1


def main() -> None:
    s = Solution()
    print(s.longestOnes([0, 1, 1, 1, 0, 1, 1], 0))
    print(s.longestOnes([0, 1, 1, 1, 0, 1, 1], 1))
    print(s.longestOnes([0, 1, 1, 0, 1, 1, 1], 0))


if __name__ == "__main__":
    main()
