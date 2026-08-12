class Solution(object):
    def replaceElements(self, nums):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l=[]
        maxp=-1
        for i in range(len(nums)-1,-1,-1):
            l.append(maxp)
            if(nums[i]>maxp):
                maxp=nums[i]
        l.reverse()
        return l
               
            
        