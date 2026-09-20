class Solution:
    def findNthDigit(self, n):
        i = 1

        while n > 9 * (10 ** (i - 1)) * i:
            n -= 9 * (10 ** (i - 1)) * i
            i += 1

        num = 10 ** (i - 1) + (n - 1) // i
        digit = (n - 1) % i

        return int(str(num)[digit])