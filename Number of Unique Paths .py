class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        lis = [[1 for i in range(a)] for j in range(b)]
        for i in range(1,len(lis)):
            for j in range(1,len(lis[0])):
                lis[i][j]=lis[i-1][j]+lis[i][j-1]
        return lis[-1][-1]
