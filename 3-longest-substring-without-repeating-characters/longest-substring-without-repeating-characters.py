class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        m=[]
        n=[]
        for i  in s:
            if(i not in m):
                m.append(i)
            else:
                n.append(len(m))
                for j in range(0,m.index(i)+1):
                    m.pop(0)
                       
                m.append(i)
        n.append(len(m))
        return max(n)
  
    