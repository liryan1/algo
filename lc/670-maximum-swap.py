class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        1. Precompute the last occurrence of every digit `last`.
        2. For every number, check if the last number exists AND occurs after.
           If yes, swap and return.
        """
        num_list = [int(n) for n in str(num)]
        last_idx = {d: idx for idx, d in enumerate(num_list)}

        for i, digit in enumerate(num_list):
            for d in range(9, digit, -1):
                to_swap_idx = last_idx.get(d, -1)
                if to_swap_idx > i:
                    num_list[i], num_list[to_swap_idx] = (
                        num_list[to_swap_idx],
                        num_list[i],
                    )
                    return int("".join(str(num) for num in num_list))

        return num


s = Solution()
print(s.maximumSwap(1993))
