#                                           Dynamic Programming using Fibonacci Series

class Solution:
    def countFriendsPairings(self, n):
        # code here 
        ctr=2
        if n<3:
            return n
        beforeprevious=1
        previous=2
        for i in range(3,n+1):
            curr = beforeprevious*ctr+previous
            
            if i==n:
                return curr % (1000000000+7)
            ctr+=1
            beforeprevious = previous
            previous = curr
            
            
