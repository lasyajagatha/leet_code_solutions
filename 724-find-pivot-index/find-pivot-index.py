class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,sum(nums)-nums[0]
        if(l+r==0):
            return 0
        c=1
        while(c<len(nums)):
            l=l+nums[c-1]
            r=r-nums[c]
            if(l==r):
                return c
            c=c+1
        return -1

        