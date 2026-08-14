class Solution(object):
    def numberOfSpecialChars(self,words):
        """
        :type word: str
        :rtype: int
        """
        c=0
        l=set(words)
        nums=list(l)
        for i in nums:
            if(i>='a' and i<='z'):
                k=i.upper()
                if(k in nums):
                    c=c+1
        return c
        