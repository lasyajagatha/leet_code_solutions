class Solution:
    def spiralOrder(self, mat: list[list[int]]) -> list[int]:
        t,l=0,0
        b,r=len(mat),len(mat[0])
        res=[]
        while(l<r and t<b):
            for i in range(l,r):
                res.append(mat[t][i])
            t=t+1
            for i in range(t,b):
                res.append(mat[i][r-1])
            r=r-1
            if(t<b):
                for i in range(r-1,l-1,-1):
                    res.append(mat[b-1][i])
                b=b-1
            if(l<r):
                for i in range(b-1,t-1,-1):
                    res.append(mat[i][l])
                l=l+1
        return res
            
            
            
                
        