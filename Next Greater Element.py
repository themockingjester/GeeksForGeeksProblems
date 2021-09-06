#                                                 Stack based solution
class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        ans=[-1 for i in range(n)]
        stackOfIndexes=[]
        for i in range(len(arr)):
            if len(stackOfIndexes)==0:
                stackOfIndexes.append(i)
            else:
                while len(stackOfIndexes)!=0 and arr[stackOfIndexes[-1]]<arr[i]:
                    val=stackOfIndexes.pop()
                    ans[val]=arr[i]
                stackOfIndexes.append(i)
        return ans
