#                                                                 Dynamic Programming 
#                                   Time -> O(N2)                                                           Space->O(N2)
class Solution:
    def maxGold(self, n, m, M):
        # code here
        ans = 0
        dp = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        
        for j in range(len(M[0])):
            for i in range(len(M)):
                
                if j==0:
                    dp[i][j]=M[i][j]
                else:
                    if i==0:
                        if len(M)==1:
                            dp[i][j]=dp[i][j-1]+M[i][j]
                        else:
                            dp[i][j]=max(dp[i][j-1],dp[i+1][j-1])+M[i][j]
                    elif i==len(M)-1:
                        dp[i][j]=max(dp[i-1][j-1],dp[i][j-1])+M[i][j]
                    else:
                        dp[i][j]=max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])+M[i][j]
                if dp[i][j]>ans:
                    ans=dp[i][j]
        
        return ans
