class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        minp=nums[0]
        maxp=-1
        for i in nums:
            if(i <minp):
                minp=i
            l.append(minp)
        for i in range(len(nums)-1,0,-1):
             t=nums[i]-l[i-1]
             if(t>maxp and t!=0):
                maxp=t
       
        return maxp

            

            
        