def reverse(S):
    
    #Add code here
    st=[]
    for i in S:
        st.insert(0,i)
    ans = ""
    for i in st:
        ans+=i
    return ans
