class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        B = [0]*len(A)
        for i in range(len(A)):
            B[i] = A[A[i]]
        for i in range(len(A)):
            A[i] = B[i+1]


    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A:
            A = A & A - 1
            count += 1
        return count

    def countSetBits(self, n):

        def numSetBits(A):
            count = 0
            while A:
                A = A & A - 1
                count += 1
            return count

        sum_ = 0
        for i in range(n + 1):
            sum_ += numSetBits(i)

        return sum_


sols = Solution()
print(sols.numSetBits(11))