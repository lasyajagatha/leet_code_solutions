class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)):
            if(i==0):
                if( i+1 < len(nums) and nums[i]>nums[i+1]):
                    return i
            elif(i==len(nums)-1 and i-1>=0):
                if(nums[i]>nums[i-1]):
                    return i
            else:
                if(nums[i]>nums[i+1] and nums[i]>nums[i-1]):
                    return i
            
        return 0