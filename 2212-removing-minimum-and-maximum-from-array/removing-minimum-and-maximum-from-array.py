class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        n=min(nums)
        o=nums.index(m)
        u=nums.index(n)
        print(o,u)
        s=0
        if(o<u):
            s=u+1
        else:
            s=o+1
        if(o<u):
            l=len(nums)-o
        else:
            l=len(nums)-u
        if(l<s):
            s=l
        if(o<u):
            l=o+1+len(nums)-u
        else:
            l=u+1+len(nums)-o
        if(l<s):
            s=l
        return s


        