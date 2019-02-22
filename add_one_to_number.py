class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s= ""
        B=[]
        if len(A)==0:
            B.append(1)
            return(B)
        else:
            for i in range(0,len(A)):
                s= s + str(A[i])
            d = int(s) + 1
            d = str(d)
            for i in range(0,len(d)):
                B.append(int(d[i]))
            return(B)