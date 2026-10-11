class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for i in range(len(nums)):
            if(len(nums)%(i+1)==0):
                s=s+nums[i]*nums[i]
        return s
        