class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        ans=0
        dp=[[0 for i in range(len(S2)+1)] for j in range(len(S1)+1)]
        for i in range(len(S1)+1):
            for j in range(len(S2)+1):
                if i==0 or j==0:
                    continue
                if S1[i-1]==S2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>ans:
                    ans = dp[i][j]
        return ans
