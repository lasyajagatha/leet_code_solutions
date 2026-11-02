class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        setofcol=set()
        setofdg1=set()
        setofdg2=set()
        res=[]
        q=[['.' for _ in range(n)]for _ in range(n)]
        def backtrack(i):
            if(i==n):
                res.append(["".join(i) for i in q])
                return
            for j in range(n):
                if(j in setofcol or (i-j) in setofdg1 or i+j in setofdg2):
                    continue
                q[i][j]='Q'
                setofcol.add(j)
                setofdg1.add(i-j)
                setofdg2.add(i+j)

                backtrack(i+1)
                setofcol.remove(j)
                setofdg1.remove(i-j)
                setofdg2.remove(i+j)
                q[i][j]='.'
        backtrack(0)
        return res

        