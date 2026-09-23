class Solution:
    def trailingZeroes(self, n):
        result = 1
        for i in range(1,n+1):
            result = result*i
        
        count = 0
        while result % 10 == 0:
            count += 1
            result = result // 10
        
        return count