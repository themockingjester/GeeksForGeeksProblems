class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        
        
        cap=W
        
        
        prof=val
        dp=[[0 for i in range(cap+1)] for j in range(len(wt)+1)]
        
        for i in range(len(wt)):
        	for j in range(len(dp[0])):
        		if j<wt[i]:
        			dp[i+1][j]=dp[i][j]
        			continue
        		dp[i+1][j]=max(dp[i][j],(prof[i]+dp[i][j-wt[i]]))
        
        return(dp[-1][-1])
