class stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.stack.pop()

    def push(self, data):
        self.stack.append(data)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        s = stack()
        for i in A:
            s.push(i)
            ar = ''

        i = s.size()
        ar = ''
        while i > 0:
            ar += s.pop()
            i -= 1
        return ar

    def reverseString2(self, A):
        i = 0
        A = list(A)
        j = len(A) - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

        return str(A)

    #reverse LL using stacks


A = "])"
Sols = Solution()
print(Sols.reverseString2(A))