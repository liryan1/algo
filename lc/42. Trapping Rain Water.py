class Solution:
    def trap(self, height: list[int]) -> int:
        water = saved_h = 0
        stack: list[tuple[int, int]] = []
        for i, h in enumerate(height):
            # Check the top of the stack and save all the trapped
            # water looking backward
            # e.g., if we had 4, 2 walls and the current height is 6
            # then we keep saving water for the lower walls until
            # we can't save water anymore, i.e. height of the top
            # element of the stack is larger than current
            while stack and stack[-1][-1] <= h:
                prev_i, prev_h = stack.pop()
                water += (min(h, prev_h) - saved_h) * (i - prev_i - 1)
                saved_h = prev_h

                # Important - logic above only saves by looking up, so it
                # cannot find water looking back. This ensures we added
                # all water we can going forward. For example
                # 4, 2, 0, 3 -> at 3, we popped 0 and 2. Then we see 4 -
                # between 3 and 4, we can trap 2 water
                if stack and stack[-1][-1] > h:
                    backwater = (min(h, stack[-1][-1]) - saved_h) * (
                        i - stack[-1][0] - 1
                    )
                    water += backwater

            stack.append((i, h))
            saved_h = h

        return water


s = Solution()
# print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(s.trap([4, 2, 0, 3, 2, 5]))
# print(s.trap([0, 1, 2, 3, 4]))
# print(s.trap([4, 3, 2, 1, 0]))
# print(s.trap([4, 3, 2, 1, 2]))
