class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        dic={']':'[',')':'(','}':'{'}
        ans=[]
        for i in x:
            if i=='(' or i=='{' or i=='[':
                ans.append(i)
            else:
                if len(ans)!=0 and ans[-1]==dic[i]:
                    ans.pop()
                else:
                    ans.append(i)
        if len(ans)==0:
            return True
        return False
