class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s=0
        i=0
        while(i<len(nums)-1):
            if(nums[i]>nums[i+1]):
                s=s+nums[i+1]
            else:
                s=s+nums[i]
            i=i+2
        return s


        