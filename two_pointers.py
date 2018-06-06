class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        # [1,2,4]
        # [2,4,5,6]
        i = 0
        i_max = len(A) - 1
        j = 0
        j_max = len(B) - 1
        res = []
        while i <= i_max and j <= j_max:
            curr_a = A[i]
            curr_b = B[j]
            if curr_a == curr_b:
                res.append(curr_a)
                i += 1
                j += 1
            elif curr_a < curr_b:
                while i <= i_max and A[i] < curr_b:
                    i += 1
            else:
                while j <= j_max and B[j] < curr_a:
                    j += 1
        return res

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # [4, 1, 1, 2, 1, 3]
    # [4, 2,  3]
    def removeElement(self, A, t):
        i = 0
        j = 0
        n = len(A)

        while i < n:
            if A[i] != t:
                A[j] = A[i]
                j += 1
            i += 1

        return j

    def sortColors(self, A):
        # @param A : list of integers
        # @return A after the sort
        n = len(A)
        a = A.count(0)
        b = A.count(1)
        for i in range(n):
            if i < a:
                A[i] = 0
            elif i < a + b:
                A[i] = 1
            else:
                A[i] = 2
        return A

    def removeDuplicates(self, A):
        n = len(A)
        if n <= 1:
            return n
        prev = A[0]
        j = 1
        for i in range(j, n):
            if prev != A[i]:
                prev = A[i]
                A[j] = A[i]
                j += 1
        return j

    # @param A : list of integers
    # @return an integer
    def removeDuplicates2(self, A):
        # A = [1, 1, 1, 2]
        # Your function should return length = 3, and A is now[1, 1, 2].
        i = 2
        fp = 2
        while i < len(A):
            if A[fp - 1] != A[i] or A[fp - 2] != A[i]:
                A[fp] = A[i]
                fp += 1
            i += 1
        return fp

    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        a = 0
        b = 0
        while a < len(A) and b < len(B):
            if A[a] > B[b]:
                A.insert(a, B[b])
                b += 1
            else:
                a += 1
        while b < len(B):
            A.append(B[b])
            b += 1

        return A

a=[4, 1, 1, 2, 1, 3]
# Sols = Solution()
# print(Sols.removeElement(a, 1))