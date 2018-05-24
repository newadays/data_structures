class Solution:
    # @param A : integer
    # @return a strings
    def genSeq(self, s):
        # s = '1211'
        j = 0
        q = ''
        while j <= len(s) - 1:
            ch = s[j]
            i = 0
            # count repitions
            while j <= len(s) - 1:
                if ch != s[j]:
                    break
                else:
                    i += 1
                    j += 1
            q += str(i) + ch
        return q

    def countAndSay(self, A):
        seq = ['1', '11', '21', '1211', '111221']

        k = len(seq) - 1
        while k <= A:
            temp = self.genSeq(seq[k])

            seq.append(temp)

            k += 1

        return seq[A - 1]

    # @param A : string
    # @return string
    def reverseWords(self, A):
        if len(A.split(" ")) > 1:
            w = ""
            words = A.split(" ")
            for i in range(len(words) - 1, -1, -1):
                w += (words[i] + " ")

            return w.rstrip()
        else:
            return A
#
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     # Implement strStr().strstr - locate a substring ( needle ) in a string ( haystack ).
#     # Try not to use standard library string functions for this question.
#     # Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#     # Good clarification questions: What should be the return value if the needle is empty?
#     # What if both haystack and needle are empty?For the purpose of this problem,
#     # assume that the return value should be -1 in both cases.
    def strStr(self, A, B):
        if A:
            words = A.split(" ")
            if len(A) == len(words):
                # words
                ls = {}
                for i in range(len(words)):
                    if B in ls:
                        return ls[words[i]]
                    else:
                        ls[words[i]] = i
                if B in ls:
                    return ls[words[i]]
                else:
                    return -1
            else:
                try:
                    words = A.index(B)
                except ValueError:
                    return -1
                if words:
                    return words

        else:
            return -1

    def letterCombinations(self, A):
        ls = {0: 0, 1: 1, 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        # m = 'abc'  # ls[A[i]] = 2
        # n = 'ghi'  # ls[A[i+1]] = 3
        A.sort()
        res = ['']
        for k in A:
            newRes = []
            for i in res:
                for j in ls[int(k)]:
                    newRes.append(i + j)
            res = newRes
        return res

sols = Solution()
print(sols.letterCombinations(list("23")))
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return a list of list of integers
#     # Given candidate set 2,3,6,7 and target 7,
#     # A solution set is:
#     # [2, 2, 3]
#     # [7]
#     def combinationSum(self, A, t):
#         ls = []

#
# def findSum(L, t, k, sum_, l):
#     rst = 0
#     while k < len(L):  # case 1: n * k = t
#         sum_ += L[k]
#         if sum_ == t:
#             k += 1
#             rst = 1
#             yield l
#
#         if rst == 1:
#             l = []
#             sum_ = 0
#             rst = 0
#         l.append(L[k])
#
#         findSum(L, t, k, sum_, l)
#
#
# A = [2,2,3]
#
# ls = []
# for i in A:
#     ls.append(list(findSum(A, 4, 0, 0, [])))
#
#
#
#
# print(ls)


# Python program to print all permutations with
# duplicates allowed

#
# def toString(List):
#     return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
# def permute(a, l, r):
#     if l == r:
#         print(toString(a))
#     else:
#         for i in range(l, r + 1):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l + 1, r)
#             a[l], a[i] = a[i], a[l]  # backtrack

# def permute(list, s):
#     if list == 1:
#         return s
#     else:
#         return [ y + x
#                  for y in permute(1, s)
#                  for x in permute(list - 1, s)
#                  ]

# print(permute(2, ["a","b","c"]))
# # Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n-1)
# sols = Solution()
# print(sols.combinationSum([ 8, 10, 6, 11, 1, 16, 8 ], 28))
# print(sols.countAndSay(7))

# def permute(A, r, l, start):
#
#     if len(start) == len(A):
#         print(start)
#         start = ''
#
#     for i in range(r, l+1):
#
#         start += A[i]
#
#         permute(A, r+1, l, start)
#
#         A[r], A[l] = A[l], A[r]
#
# a=["a","b","c"]
# n = len(a)
# permute(a, 0, n-1, '')


