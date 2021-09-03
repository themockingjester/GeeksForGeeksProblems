#                                 Dynamic Programming (an variation of longest common subsequece)
class Solution:

    def longestPalinSubseq(self, S):
        x=len(S)
        y=len(S)
        s1=S
        s2=S[::-1]
        # code here
        dp=[[0 for i in range(x+1)] for j in range(y+1)]
        for i in range(y+1):
            
            for j in range(x+1):
                if i==0 or j==0:
                    continue
                
                
                
                if s2[i-1]==s1[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
