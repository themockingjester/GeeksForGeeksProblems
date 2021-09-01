#                             Brute force approach
class Solution:
	def editDistance(self, s, t):
		# Code here
		self.min=999999
		self.recur("",0,0,s,t,0)
		return self.min
	def recur(self,ans,currIndexFirst,currIndexSecond,a,b,ctr):
        if ans==b:
            if ctr<self.min:
                self.min=ctr
            return
        elif len(a)>currIndexFirst and len(b)>currIndexSecond:
            if a[currIndexFirst]==b[currIndexSecond]:
                self.recur(ans+a[currIndexFirst],currIndexFirst+1,currIndexSecond+1,a,b,ctr)
            else:
                self.recur(ans,currIndexFirst+1,currIndexSecond,a,b,ctr+1)                 # not including
                self.recur(ans+b[currIndexSecond],currIndexFirst+1,currIndexSecond+1,a,b,ctr+1)                 # replacing
                self.recur(ans+b[currIndexSecond],currIndexFirst,currIndexSecond+1,a,b,ctr+1)                 #inserting
        else:
            return


#                            Dynamic Programming (Bottom Up Approach)
class Solution:
	def editDistance(self, s, t):
		# Code here
		dp=[[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
		for i in range(len(t)+1):
		    
		    for j in range(len(s)+1):
		        
		        if i==0 and j==0:
		            dp[i][j]=0
		        elif j==0:
		            dp[i][j]=1+dp[i-1][j]
		        elif i==0:
		            dp[i][j]=1+dp[i][j-1]
		        else:
		            if s[j-1]==t[i-1]:
		                dp[i][j]=dp[i-1][j-1]
		            else:
		                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
		return dp[-1][-1]
		            
		        
