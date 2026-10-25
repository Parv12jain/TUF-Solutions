class Solution:
    def missingNumber(self, nums):
        total = 0
        actual = 0
        n = len(nums)

        for i in range(0,n):
            actual+=nums[i]

        for i in range(0,n+1):
            total+=i
        
        return total - actual

        