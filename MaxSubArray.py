class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        final_sum = A[0]
        tmp = 0
        for i in A[1:]:
            tmp = tmp + i
            if max(tmp, final_sum) == tmp:
                final_sum = tmp
            if tmp < 0:
                tmp = 0
        return final_sum