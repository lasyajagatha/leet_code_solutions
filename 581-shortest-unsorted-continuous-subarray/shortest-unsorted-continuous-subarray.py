class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=sorted(nums)
        l,r=-1,-1
        for i in range(0,len(nums)):
            if(nums[i]!=a[i]):
                l=i
                break
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]!=a[i]):
                r=i
                break
        if(l<r):
            return r-l+1
        else:
            return 0
     
           

        