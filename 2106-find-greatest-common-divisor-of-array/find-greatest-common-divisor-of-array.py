class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        n=min(nums)
        l=0
        for i in range(1,n+1):
            if(m%i==0 and n%i==0):
                if(i>l):
                    l=i
        return l

        