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


sols = Solution()
print(sols.countAndSay(7))



