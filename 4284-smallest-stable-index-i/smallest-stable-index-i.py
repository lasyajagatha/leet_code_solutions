class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(0,len(nums)):
            u=max(nums[:i+1])
            v=min(nums[i:])
            if((u-v)<=k):
                return i
        return -1
        