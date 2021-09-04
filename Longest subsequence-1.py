#                                    Dynamic Programming                                   Time-> O(N2)                           Space->O(N)
#                       Note:- This approach throws TLE on GeeksForGeeks

class Solution:
    def longestSubsequence(self, N, A):
        # code here
        ans=0
        dp=[1 for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A)):
                if j>i and abs(A[i]-A[j])==1:
                    dp[j]=dp[i]+1
                if dp[j]>ans:
                    ans=dp[j]
        return ans
