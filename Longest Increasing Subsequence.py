import bisect
class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        lis=[]
        for i in a:
            if len(lis)==0:
                lis.append(i)
            elif i>lis[-1]:
                lis.append(i)
            else:
                lis[bisect.bisect_left(lis,i)]=i
        return len(lis)
