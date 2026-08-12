class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        s=0
        for i in nums:
            if(i in l):
                continue
            if(nums.count(i)==1):
                s=s+i
            else:
                l.append(i)

        return s
        