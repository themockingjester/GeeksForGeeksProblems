class Solution:
    
    
    
    def solve(self,cr,cc,rows,cols,m,path):
        if cr==rows-1 and cc==cols-1:
            
                
            self.ans.append(path)
            return
        if cr<0 or cc<0 or cr>=rows or cc>= cols or m[cr][cc]==0:
            return
        if self.mat[cr][cc]!=0:
            return
        
        self.mat[cr][cc]=1
        self.solve(cr+1,cc,rows,cols,m,path+'D')
        self.solve(cr-1,cc,rows,cols,m,path+'U')
        self.solve(cr,cc+1,rows,cols,m,path+'R')
        self.solve(cr,cc-1,rows,cols,m,path+'L')
        self.mat[cr][cc]=0
    def findPath(self, m, n):
        if m[-1][-1]==0:
            return []
        self.ans=[]
        self.mat=[[0 for i in range(n)] for j in range(n)]
        self.solve(0,0,len(m),len(m[0]),m,"")
        return sorted(self.ans)
