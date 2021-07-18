class Solution:
    def check(self,n):
        if n==0:
            return 0
        sumis=0
        for i in [2,3,4]:
            
            if n//i in self.dic:
                sumis+=self.dic[n//i]
            else:
                
                temp=self.check(n//i)
                self.dic[n//i]=max(n//i,temp)
                sumis+=temp
        return max(sumis,n)
                
    def maxSum(self, n): 
        
        self.dic={}
        if n==0:
            return 0
        # code here 
        t=self.check(n)
        
        return t
