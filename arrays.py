class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        maxi = -1
        i = 0
        a = []
        while i < len(A):
            while i < len(A) and A[i] < 0:
                i += 1
            l = []
            while i < len(A) and A[i] >= 0:
                l.append(A[i])
                i += 1

            if sum(l) > maxi:
                a = l
                maxi = sum(l)

        return a

    def genSubsets(self, arr):
        # @param A : list of integers
        # @return subsets of A
        i = 0
        s = []
        while i < len(arr):
            j = 0
            while j <= len(arr):
                r = arr[i:i + j]
                if r not in s:
                    s.append(r)
                    # print(s)
                j += 1
            i += 1
        return s

    # The ordered quadruplet of (7, 4, 0, 9)
    # whose sum is 20. Notice that there
    # are two other quadruplets whose sum is 20:queen
    # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
    # asked to return the just one quadruplet (in an
    # ascending order)
    def find_array_quadruplet(self, A, t):
        n = len(A)
        for a in range(n):
            for b in range(a+1, n):
                sum_ab = A[a] + A[b]
                seen_numbers = {}
                possible_c_d = []

                for d in range(a+1, n):
                    if t-(sum_ab+A[d]) in seen_numbers:
                        c = seen_numbers[t-(sum_ab+A[d])]
                        if b != c and c != d:
                            possible_c_d.append([c, d])
                    else:
                        if d not in seen_numbers and b != d:
                            seen_numbers[A[d]] = d

                if len(possible_c_d) > 0:
                   c,d = (list(sorted(possible_c_d)))[0]
                   return sorted([A[a], A[b], A[c], A[d]])

    def findDuplicates(self, A):

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Input:
        # [4,3,2,7,8,2,3,1]
        # Output:
        # [2,3]
        i = 0
        ls = {}
        res = {}
        while i < len(A):
            if A[i] in ls:
                res[A[i]] = i
            else:
                ls[A[i]] = A[i]
            i += 1

        return list(res.keys())

Sols = Solution()
a = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
# print(findQuad(a, s))
print(Sols.find_array_quadruplet(a, s))


def generate(A):
    if A <= 0:
        return []
    result = [[1]]
    for r in range(1, A):
        row = [1]
        for i in range(1, r):
            row.append(result[r - 1][i - 1] + result[r - 1][i])
        row.append(1)
        result.append(row)
    return result

print(generate(3))



