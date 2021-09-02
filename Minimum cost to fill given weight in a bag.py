        # Dynamic Programming                           Time-> O(N2)           Space-> O(N)
class Solution:
    def minimumCost(self, cost, n, W):
        dp=[9999999 for i in range(W+1)]
        dp[0]=0
        for i in range(len(cost)):
            
            for j in range(W+1):
                if j==0:
                    continue
                elif j==i+1 and dp[j]==0 and cost[i]!=-1:
                    dp[j]=cost[i]
                    continue
                if j>=i+1 and cost[i]!=-1:
                    dp[j]=min(dp[j],(dp[j-(i+1)]+cost[i]))
        if dp[-1]==9999999:
            return -1
        return dp[-1]
                
