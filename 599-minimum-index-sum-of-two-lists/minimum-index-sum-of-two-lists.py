class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l=[]
        min=2**31
        for i in list1:
            if(i in list2):
                u=list1.index(i)
                v=list2.index(i)
                if(u+v < min):
                    if(l!=[]):
                       l.pop(0)
                    min=u+v
                    l.append(i)
                elif u+v==min:
                    l.append(i)
        return l

        