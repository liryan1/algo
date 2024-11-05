# get all existing islands, store in map
# go through all 0s, check all neighbors it is connected to by flipping it


class Solution:
    def dfs(self, x, y, n, grid, index):
        size = 0
        grid[x][y] = index
        for i, j in self.move(x, y, n):
            if grid[i][j] == 1:
                size += self.dfs(i, j, n, grid, index)
        return size + 1

    def move(self, x, y, n):
        for i, j in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if 0 <= i < n and 0 <= j < n:
                yield i, j

    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)

        index = 2  # start at 2 to prevent conflict
        sizes = {}  # island index, side
        # Mark islands by index and calculate sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[index] = self.dfs(i, j, n, grid, index)
                    index += 1
        if not sizes:
            return 1

        largest = max(sizes.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # Don't count the same island
                    neighbors = set(
                        grid[x][y] for x, y in self.move(i, j, n) if grid[x][y]
                    )
                    # flip the 1 to get a new area
                    new_area = 1 + sum(sizes[i] for i in neighbors)
                    largest = max(largest, new_area)

        return largest
