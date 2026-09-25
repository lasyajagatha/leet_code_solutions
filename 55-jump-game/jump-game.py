class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m=0
        for i in range(0,len(nums)):
            if(i>m):
                return False
            if(m<i+nums[i]):
                m=i+nums[i]
            if(m>=len(nums)-1):
                return True
        return True
