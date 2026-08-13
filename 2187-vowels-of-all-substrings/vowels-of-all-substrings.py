class Solution(object):
    def countVowels(self, nums):
        """
        :type word: str
        :rtype: int
        """
        c=0
        p=['a','e','i','o','u']
        for i in range(0,len(nums)):
            if(nums[i] in p):
                c=c+((len(nums)-i)*(i+1))
        return c

        