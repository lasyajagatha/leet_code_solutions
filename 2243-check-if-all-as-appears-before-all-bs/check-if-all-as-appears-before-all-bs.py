class Solution:
    def checkString(self, s: str) -> bool:
        if('b' not in s):
            return True
        l=s.index("b")
        for i in range(l+1,len(s)):
            if(s[i]=='a'):
                return False
        return True
        