class Solution:
    def myPowRecursive(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:  # handle negative powers
            n = -n
            x = 1 / x
        prev = self.myPowRecursive(x, n // 2)
        result = prev * prev
        if n & 1:  # if n is odd, // 2 rounds down, so multiply by another x
            result *= x
        return result

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x

        power = 1.0
        while n:
            if n & 1:  # same as num % 2 != 0
                power *= x
            x *= x
            n //= 2

        return power
