class Solution:
    def findGCD(self, nums):
        min = nums[0]
        max = nums[0]

        for i in range(0,len(nums)):
            if nums[i]<min :
                min = nums[i]
            elif nums[i]>max :
                max = nums[i]
        
        for i in range(1, min + 1):
            if min% i == 0 and max % i == 0:
                gcd = i

        return gcd 