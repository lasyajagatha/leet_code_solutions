class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=[]
        l=[]
        p=[]
        o=0
        for i in nums:
            if(i>0):
                k.append(i)
            else:
                l.append(i)
        for i in range(0,len(nums)):
            if(i%2==0):
                p.append(k[o])
            else:
                p.append(l[o])
                o=o+1
        return p
