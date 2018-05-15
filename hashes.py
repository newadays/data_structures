class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        lst = {}
        for i, v in enumerate(A):
            if B - v in lst:
                return lst[B - v] + 1, i + 1
            elif v not in lst:
                lst[v] = i
        return []

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        d = {}
        for i in range(len(A)):
            tmp1 = B + A[i]
            tmp2 = A[i] - B
            if tmp1 in d or tmp2 in d:
                return 1
            else:
                d[A[i]] = True
        return 0


A = [ 34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29 ]
Solution = Solution()
print(Solution.twoSum([2, 7, 11, 15], 9))
print(Solution.diffPossible([2, 7, 11, 15], 9))


