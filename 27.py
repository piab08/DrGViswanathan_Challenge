class Solution:
    def arraySign(self, nums):
        prod = 1
        for n in nums :
            prod = prod*n
        
        if prod>0 :
            return 1
        elif prod<0 :
            return -1
        else :
            return 0
        