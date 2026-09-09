class Solution:
    def plusOne(self, digits):
        num = 0

        for i in digits:
            num = num * 10 + i

        num = num + 1

        result = []

        while num != 0:
            r = num % 10
            result.append(r)
            num = num // 10

        result.reverse()
        return result