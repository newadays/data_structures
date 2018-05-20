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

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


class Solution:
    # reverse LL using stacks
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

    #Balance Parentheses
    # @param A : string
    # @return an integer
    def isValid(self, A):
        s = stack()
        ar = {"(":")", "[":"]", "{":"}"}
        for i in A:
            if i in ar:
                s.push(i)
            else:
                if s.is_empty():
                    return 0
                else:
                    if ar[s.top()]!=i:
                        return 0
                    else:
                        s.pop()
        if s.size() > 0:
            return 0
        else:
            return 1

    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        height = A
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans

# A = "[{"
Sols = Solution()
# print(Sols.reverseString2(A))
# print(Sols.isValid(A))
print(Sols.largestRectangleArea([2,1,5,6,2,3]))

