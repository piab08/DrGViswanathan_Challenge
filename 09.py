class Solution:
    def isPalindrome(self, n):
        if n < 0:
            return False

        temp = n
        r = 0

        while n != 0:
            digit = n % 10
            r = (r * 10) + digit
            n = n // 10

        return temp == r