class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        min = 0
        if len(A)>1  :
            for i in range(1,len(A)):
              min += max(abs(A[i] - A[i-1]),abs(B[i] - B[i-1]))
    
            return(min)
        else:
            return(0)