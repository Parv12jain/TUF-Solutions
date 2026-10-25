class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        zeros = []
        non_zeros = []
        for i in range(0,n):
            if nums[i] == 0:
                zeros.append(nums[i])
            else:
                non_zeros.append(nums[i])

        nums[:] = non_zeros + zeros

        return nums