def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


# fib with memoization
def fib_memo(n, memo):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = result
    return result


memo = {}


# bottom up approach
# No need for recursive calls on the call stack
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return n
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

    return bottom_up[n]


print(fib_memo(10, memo))
# print(fib_bottom_up(10))

#Count  Longest Increasing subarray
# @param A : tuple of integers
# @return an integer
def lis(A):
    n = len(A)
    ls = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if A[i] > A[j] and ls[i] < ls[j] + 1:
                ls[i] = ls[j] + 1
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, ls[i])

    return maximum

# @param A : string "aaa",
# @param B : string "aa"
# @return an integer
def isMatch(A, B):
    n1 = len(A)
    n2 = len(B)
    if not n1 and not n2:
        return 1
    if not n2:
        return 0
    i = 0
    j = 0
    star = None
    curr_i = None
    #print('HERE1')
    while i < n1:
        if j < n2 and (A[i] == B[j] or B[j] == '?'):
            i += 1
            j += 1
        elif j < n2 and B[j] == '*':
            #print('HERE2')
            star = j
            j += 1
            curr_i = i
        elif star is not None:
            #print('HERE3')
            curr_i += 1
            i = curr_i
            j = star + 1
        else:
            #print('HERE4')
            return 0
    while j < n2 and B[j] == '*':
        j += 1
    #print('HERE5')
    return 1 if j == n2 else 0


print(isMatch("aa", "a*"))