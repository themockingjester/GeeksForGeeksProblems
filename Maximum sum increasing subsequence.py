class Solution:
	def maxSumIS(self, Arr, n):
		# code here
        dp = Arr.copy()
        for i in range(n):
            for j in range(i):
                if Arr[j]<Arr[i]:
                    dp[i]=max(dp[i],dp[j]+Arr[i])
        return max(dp)
