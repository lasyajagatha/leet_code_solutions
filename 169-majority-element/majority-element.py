class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        c=0
        m=0
        o=nums[0]
        k=len(nums)
        for i in nums:
            if(i not in l):
                if(nums.count(i)>m):
                    m=nums.count(i)
                    o=i
                if(m>k/2):
                    return o
                l.append(i)
        return o


           
           