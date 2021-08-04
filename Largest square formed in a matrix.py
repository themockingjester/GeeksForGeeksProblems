'''

Given a binary matrix mat of size n * m, find out the maximum size square sub-matrix with all 1s.

Example 1:

Input: n = 2, m = 2
mat = {{1, 1}, 
       {1, 1}}
Output: 2
Explaination: The maximum size of the square
sub-matrix is 2. The matrix itself is the 
maximum sized sub-matrix in this case.

Example 2:

Input: n = 2, m = 2
mat = {{0, 0}, 
       {0, 0}}
Output: 0
Explaination: There is no 1 in the matrix.

Your Task:
You do not need to read input or print anything. Your task is to complete the function maxSquare() which takes n, m and mat as input parameters and returns the size of the maximum square sub-matrix of given matrix.

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1 ≤ n, m ≤ 50
0 ≤ mat[i][j] ≤ 1 
'''
class Solution:
    def check(self,cr,cc,n,m):
        if cr>=n or cr<0 or cc>=m or cc<0:
            return 999999999
        
        return self.res[cr][cc]
    def maxSquare(self, n, m, mat):
        # code here
        maxi=0
        self.res=[[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        for cr in range(len(mat)):
            
            for cc in range(len(mat[0])):
                if cc==0 or cr==0:
                    self.res[cr][cc]=mat[cr][cc]
                else:
                    if mat[cr][cc]==0:
                        self.res[cr][cc]=0
                    else:
                        val=min(self.check(cr-1,cc-1,n,m),self.check(cr-1,cc,n,m),self.check(cr,cc-1,n,m))
                        self.res[cr][cc]=mat[cr][cc]+val
                if self.res[cr][cc]>maxi:
                    maxi=self.res[cr][cc]
                            
        return maxi
