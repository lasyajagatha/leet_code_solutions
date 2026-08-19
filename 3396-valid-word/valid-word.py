class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        l=['a','e','i','o','u','A','E','I','O','U']
        f=['1','2','3','4','5','6','7','8','9','0']
        c=0
        k=0
        print(word)
        p=0
        for i in word:
            if(i>='a' and i<='z' or i>='A' and i<='Z' ):
                if(i in l):
                    c=1
                else:
                    k=1
                p=p+1
            elif ( i in f):
                p=p+1
            else:
                return False
        print(p,k,c)
        if(p>=3 and c==1 and k==1):
            return True
        return False
           
        