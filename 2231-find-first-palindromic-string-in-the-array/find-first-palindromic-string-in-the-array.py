class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        k=[]
        for i in words:
            k.append(i[::-1])
        for i in range(0,len(words)):
            if(words[i]==k[i]):
                return words[i]
        return ""

        