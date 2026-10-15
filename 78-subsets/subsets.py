class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=[[]]
        for i in nums:
            r=[]
            for j in l:
                r.append(j+[i])
            print(r)
            for i in r:
                l.append(i)
        return l
