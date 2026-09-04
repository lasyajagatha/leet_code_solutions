class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        a=0
        for i in word:
            if(i>='A' and i<='Z'):
                a=a+1
        if(a==len(word) or (a==1 and (word[0]>='A' and word[0]<='Z')) or a==0):
            return True
        else:
            return False


        