class Solution:
    def getNextIndex(self, i: int, j: int, m: int, n: int) -> tuple[int, int]:
        # if i + j is even, then try to go up right (-1, +1), if can't then
        #   go right, if can't then down
        # if i + j is odd, then try to go down left (+1, -1), if can't then
        #   go down, if can't then right
        def isValid(i: int, j: int, m: int, n: int) -> bool:
            return (0 <= i < m) and (0 <= j < n)

        if (i + j) & 1:
            if isValid(i + 1, j - 1, m, n):
                return i + 1, j - 1
            elif isValid(i + 1, j, m, n):
                return i + 1, j
            elif isValid(i, j + 1, m, n):
                return i, j + 1
        else:
            if isValid(i - 1, j + 1, m, n):
                return i - 1, j + 1
            elif isValid(i, j + 1, m, n):
                return i, j + 1
            elif isValid(i + 1, j, m, n):
                return i + 1, j

        return i, j

    def findDiagonalOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])

        i = j = 0
        result = [matrix[0][0]]
        while not (i == m - 1 and j == n - 1):
            i, j = self.getNextIndex(i, j, m, n)
            result.append(matrix[i][j])

        return result
