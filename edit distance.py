#                             Brute force approach
class Solution:
	def editDistance(self, s, t):
		# Code here
		self.min=999999
		self.recur("",0,0,s,t,0)
		return self.min
	def recur(self,ans,currIndexFirst,currIndexSecond,a,b,ctr):
        if ans==b:
            if ctr<self.min:
                self.min=ctr
            return
        elif len(a)>currIndexFirst and len(b)>currIndexSecond:
            if a[currIndexFirst]==b[currIndexSecond]:
                self.recur(ans+a[currIndexFirst],currIndexFirst+1,currIndexSecond+1,a,b,ctr)
            else:
                self.recur(ans,currIndexFirst+1,currIndexSecond,a,b,ctr+1)                 # not including
                self.recur(ans+b[currIndexSecond],currIndexFirst+1,currIndexSecond+1,a,b,ctr+1)                 # replacing
                self.recur(ans+b[currIndexSecond],currIndexFirst,currIndexSecond+1,a,b,ctr+1)                 #inserting
        else:
            return
