class Solution:
    def knapSack(self, N, W, val, wt):
        
        cap=W
        
        n=N
        
        prof=val
        
        
        dp=[0]*(cap+1)
        for i in range(0,len(wt)):
        	
        	for j in range(len(dp)):
        		if j<wt[i]:
        			continue
        		dp[j]=max((dp[j-wt[i]]+prof[i]),dp[j])
        return(dp[-1])
