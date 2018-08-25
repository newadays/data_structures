class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, n):
        ls = ['1', '11', '21', '1211', '111221']

        def genCand(item):
            i = 0
            rs = ''
            while i <= len(item) - 1:
                j = 0
                while j + i <= len(item) - 1:
                    if item[i] != item[j + i]:
                        break
                    else:
                        j += 1
                rs += str(j) + str(item[i])
                i += j
            return rs

        if n < len(ls):
            return ls[n - 1]
        else:
            i = len(ls) - 1
            while i < n - 1:
                result = str(genCand(ls[i]))
                ls.append(result)
                i += 1

        return ls[n - 1]

    # @param A : string
    # @return string
    def reverseWords(self, A):
        if len(A) > 1:
            words = ''
            a = A.split(" ")
            for i in range(len(a) - 1, -1, -1):
                words += a[i] + " "
            return words.strip()
        else:
            return A.strip()

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if not paragraph:
            return ''
        banned = [x.lower() for x in banned]
        paragraph.lower()
        p = paragraph.split(" ")
        p = [x.strip("!?',;.").lower() for x in p]
        cnt = -1
        for word in p:
            if word not in banned:

                if cnt < p.count(word):
                    res = word
                    cnt = p.count(word)
        return res

    # @param A : string
    # @param B : string
    # @return an integer
    # Implement strStr().strstr - locate a substring ( needle ) in a string ( haystack ).
    # Try not to use standard library string functions for this question.
    # Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    # Good clarification questions: What should be the return value if the needle is empty?
    # What if both haystack and needle are empty?For the purpose of this problem,
    # assume that the return value should be -1 in both cases.
    def strStr(self, A, B):
        if A:
            res = None
            if len(A.split(' ')) > 1:
                A = A.split(' ')
                ls = {}
                for i in range(len(A)):
                    if B in ls:
                        return ls[B]
                    else:
                        if A[i] not in ls:
                            ls[A[i]] = i
            else:
                try:
                    res = A.index(B)
                except ValueError:
                    return -1
                if res is not None:
                    return res
            return -1
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        ls = {'0': '0', '1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']
        for i in A:
            newRes = []
            for j in res:
                for k in ls[i]:
                    newRes.append(j + k)
            res = newRes
        return res

sols = Solution()
print(sols.letterCombinations(list("234")))


def longestCommonPrefix(A):
    i = 0
    new = ''
    if len(A) == 1:
        return A[0]
    else:

        while (True):

            try:
                for k in range(1, len(A)):

                    if A[k - 1][i] != A[k][i]:
                        return new

                print(k)
                new += A[k - 1][i]
                # print(new)
                i += 1

            except:

                return new

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):


        sum_ = 0
        for i in B:
            sum_ += hash(i)
        # ["foo", "bar"]
        l, lw = len(B), len(B[0])
        start = 0
        end = l * lw
        res = []
        # if len(list(set(list(A)))) == len(list(set(B))):
        #     return list(range(0, len(A) - end + 1))
        # "barfoothefoobarman"
        while start <= len(A):
            word = A[start:end]
            # print(word)
            j = 0
            k = lw
            sum_2 = 0
            while j <= len(word):
                sum_2 += hash(word[j:k])
                j += lw
                k += lw
            if sum_ == sum_2:
                res.append(start)
            start += 1
            end += 1

        return res

    def strStr(self, A, B):
        # @param A : string
        # @param B : string
        # @return an integer
        for i in range(len(A)):
            if A[i] == B[0]:
                if B[0::] == A[i:i + len(B)]:
                    return i
        return -1


