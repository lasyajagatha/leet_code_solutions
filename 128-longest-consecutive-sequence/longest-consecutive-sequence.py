class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if(nums==[]):
            return 0
        l=[]
        c=0
        seen=[]
        for i in range(0,len(nums)-1):
            if(nums[i]+1==nums[i+1]):
                c=c+1
            elif (nums[i]==nums[i+1]):
                continue
            else:
                if(c!=0):
                    l.append(c)
                c=0
        l.append(c)
        return max(l)+1
        