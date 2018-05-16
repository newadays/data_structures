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
        lst = {}
        for i, v in enumerate(A):
            if (v + B in lst) and (i != lst[v + B]):
                return 1
            elif v - B in lst and i != lst[v - B]:
                return 1
            else:
                lst[v] = i
            return 0

    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers

    # 	S: "barfoothefoobarman"
    # L: ["foo", "bar"]
    def findSubstring(self, A, B):
        from collections import Counter
        if len(B) > 0:
            cand_sum = 0
            # store unique values of B
            for word in B:
                cand_sum += hash(word)
            # iterate through the entire string
            l, lw = len(B), len(B[0])
            l_str = len(A)
            result = []
            start = 0
            end = lw * l
            #same characters and repeated words
            c = dict(Counter(A))
            if len(list(set(B))[0]) == len(B[0]) and len(c) == 1:
                if len(c) == len(list(set(B))):
                    return list(range(len(A) - end + 1))

            while start <= l_str:
                words = A[start:end]
                sum_words = 0
                i = 0
                j = lw

                while i < len(words):
                    sum_words += hash(words[i:j])
                    i += lw
                    j += lw

                if cand_sum == sum_words:
                    result.append(start)
                start += 1
                end += 1
            return result

        else:
            return []


A = [34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98,
     69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29]
Solution = Solution()
print(Solution.twoSum(A, 25))
print(Solution.diffPossible([2, 7, 11, 15], 9))
# S = "barfoothefoobarman"
# L = ["foo", "bar"]
S = "abbaccaaabcabbbccbabbccabbacabcacbbaabbbbbaaabaccaacbccabcbababbbabccabacbbcabbaacaccccbaabcabaabaaaabcaabcacabaa"
L = [ "cac", "aaa", "aba", "aab", "abc" ]
print(Solution.findSubstring(S, L))
