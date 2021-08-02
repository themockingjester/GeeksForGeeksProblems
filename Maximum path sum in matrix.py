'''
                                                            Dynamic Programming

Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].

    Matrix [r+1] [c]
    Matrix [r+1] [c-1]
    Matrix [r+1] [c+1]

Starting from any column in row 0 return the largest sum of any of the paths up to row N-1.

Example 1:

Input: N = 2
Matrix = {{348, 391},
          {618, 193}}
Output: 1009
Explaination: The best path is 391 -> 618. 
It gives the sum = 1009.


Example 2:

Input: N = 2
Matrix = {{2, 2},
          {2, 2}}
Output: 4
Explaination: No matter which path is 
chosen, the output is 4.


Your Task:
You do not need to read input or print anything. Your task is to complete the function maximumPath() which takes the size N and the Matrix as input parameters and returns the highest maximum path sum.


Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N*N)


Constraints:
1 ≤ N ≤ 500
1 ≤ Matrix[i][j] ≤ 1000
'''
class Solution:
    def check(self,cr,cc,m,n,Matrix):
        if cc<0 or cr<0 or cc>=n or cr>=m:
            return 0
        return Matrix[cr][cc]
        
    def maximumPath(self, N, Matrix):
         #code here
        for cr in range(len(Matrix)):
            for cc in range(len(Matrix[0])):
                if cr==0:
                    pass
                else:
                    Matrix[cr][cc]=max(self.check(cr-1,cc-1,len(Matrix),len(Matrix[0]),Matrix),self.check(cr-1,cc,len(Matrix),len(Matrix[0]),Matrix),self.check(cr-1,cc+1,len(Matrix),len(Matrix[0]),Matrix))+Matrix[cr][cc]
                    
                
         
        return max(Matrix[-1][:])
