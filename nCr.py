class Solution:
    
        
    def nCr(self, n, r):
        
        self.dic={}
        # code here
        if r>n:
            return 0
        elif r==n:
                    self.dic[ctr]=pro
        else:
            pro=1
            ctr=1
            while ctr<=n:
                
                pro = pro*ctr
                if ctr==n or ctr==n-r or ctr==r:
                    self.dic[ctr]=pro
                ctr+=1
            res=self.dic[n]//(self.dic[r]*self.dic[n-r])
            return res % (1000000000+7)
