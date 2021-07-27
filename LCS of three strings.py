class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        dp=[[[0 for i in range(len(A)+1)] for j in range(len(B)+1)] for k in range(len(C)+1)]
        for k in range(1,len(C)+1):
            for j in range(1,len(B)+1):
                for i in range(1,len(A)+1):
                    if C[k-1]==B[j-1] and C[k-1]==A[i-1]:
                        dp[k][j][i]=dp[k-1][j-1][i-1]+1
                    else:
                        dp[k][j][i]=max(dp[k-1][j][i],dp[k][j-1][i],dp[k][j][i-1])
        return dp[-1][-1][-1]
                    
