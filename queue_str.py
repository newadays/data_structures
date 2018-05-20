class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
            #

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

A = [1,4,5,10,2]
q = queue()
for i in A:
    q.enqueue(i)

print(q.size())


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        for ch in A:
            if ch in "+-*/":
                arg2 = stack.pop()
                arg1 = stack.pop()

                if ch is "+":
                    stack.append(arg1 + arg2)
                if ch is "-":
                    stack.append(arg1 - arg2)
                if ch is "*":
                    stack.append(arg1 * arg2)
                if ch is "/":
                    stack.append(arg1 // arg2)
            else:
                stack.append(int(ch))

        return stack.pop()


A = [ "5", "1", "2", "+", "4", "*", "+", "3", "-" ]
Sols = Solution()
print(Sols.evalRPN(A))