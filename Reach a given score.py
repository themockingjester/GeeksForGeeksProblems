'''

                                                                     Dynamic Programming

Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.

Example:
Input
3
8
20
13
Output
1
4
2
Explanation
For 1st example when n = 8
{ 3, 5 } and {5, 3} are the 
two possible permutations but 
these represent the same 
cobmination. Hence output is 1.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function count( ) which takes N as input parameter and returns the answer to the problem.

Constraints:
1 ≤ T ≤ 100
1 ≤ n ≤ 1000

'''

def count(n):
    #your code here
    dp=[0 for i in range(n+1)]
    dp[0]=1
    for i in [3,5,10]:
        
        for j in range(len(dp)):
            if j>=i:
                dp[j]=dp[j-i]+dp[j]
    
    return dp[-1]
