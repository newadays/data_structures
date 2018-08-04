#iterative
def binarySearch_iter(A, start, ending, num):
    while start <= ending:
        m = round((start+ending)/2)
        if num == A[m]:
            return m
        else:
            if A[m] < num:
                start = m+1
            else:
                ending = m-1
    return -1

# recursion
def binarySearch(A, start, ending, num):

    if start > ending:
        return -1
    m = round((start+ending)/2)
    if num == A[m]:
        return m
    elif num < A[m]:
        return binarySearch(A, start, m-1, num)
    else:
        return binarySearch(A, m+1, ending, num)


A = [-1, -1, 2, -1, -1, -1, 5]
A.sort()
# A = [ 44, 41, 12, 42, 71, 45, 28, 65, 75, 93, 66, 66, 37, 6, 24, 59 ]


print(binarySearch(A, 0, len(A), 5))

#binary search with return of first, last pos


def binarySearchPos(A, start, ending, num, fpos):
    ending -= 1
    result = 0
    while start <= ending:
        m = round((start+ending)/2)
        if num == A[m]:
            result = m
            if fpos is True: #first num occurence
                ending = m-1
            else:          #last num occurence
                start = m+1
        elif num < A[m]:
            ending = m-1
        else:
            start = m+1
    return result


# A=[2,3,3,4,10,10,10,18,20]
A = [-3,-3,2,-1,-1,-1,5]
A.sort()
print(binarySearchPos(A, 0, len(A), -3, False))


def findCount(A, n, x):
    # @param A: list of integers, size & x to find
    # @return the number of occurrence of x in A
    count = 0

    def findPos(a, siz, num, d):
        start = 0
        ending = siz - 1
        pos = -1
        while start <= ending:
            m = round((start + ending) / 2)
            if num == a[m]:
                pos = m
                if d is True:
                    ending = m - 1
                else:
                    start = m + 1
            elif num < a[m]:
                ending = m - 1
            else:
                start = m + 1

        return pos

    firstpos = findPos(A, n, x, True)

    if firstpos == -1:
        return count
    else:
        lastpos = findPos(A, n, x, False)
        count = lastpos - firstpos + 1

    return count


# A=[2,3,3,4,10,10,10,18,20]
A = [-3, -3, 2, -1, -1, -1, 5]
A.sort()
print(findCount(A, len(A), -3))


def countRotate(A):
    # @params: rotated list A
    # return: no of times A was rotated

    def findPivot(A, n):
        l = n - 1
        s = 0
        while s <= l:
            m = round((s + l) / 2)
            if A[s] < A[l]:
                return s

            n_m = (m + 1) % n
            p_m = (m - 1 + n) % n

            if (A[m] <= A[n_m]) and (A[m] <= A[p_m]):
                return m

            elif A[m] <= A[l]:
                l = m - 1

            elif A[m] >= A[s]:
                s = m + 1

    if len(A) < 2:
        return 1
    else:
        pos = findPivot(A, len(A))
        return pos


#
A = [15, 17, -1, 1, 5, 4, 6, 7, 8, 9]
# A = [5, -3, -3, -1, -1, -1, 4]
print(countRotate(A))


def searchRotated(A, n, x):
    # params - sorted distinct rotated array A,size of A & element to search
    # return - position of element
    l = n - 1
    s = 0
    while s <= l:
        m = round((s + l) / 2)
        if x == A[m]:
            return m
        elif A[m] <= A[l]:
            if (x > A[m]) and (x <= A[l]):
                s = m + 1
            else:
                l = m - 1
        elif A[m] <= A[s]:
            if (x >= A[l]) and (x < A[m]):
                l = m - 1
            else:
                s = m + 1
        else:
            return -1


#
# A=[15,17,-1,1,4,5,6,7,8,9]
A = [5, 6, -3, -1, 0, 4]
print(searchRotated(A, len(A), -3))


def bst_count(arr, num):
    def bst(A, x, pos):
        lo, hi, result = 1, len(A) - 1, -1
        while lo <= hi:
            m = lo + (hi - lo) // 2

            if x == A[m]:
                result = m
                if pos:
                    hi = m - 1
                else:
                    lo = m + 1

            elif x < A[m]:
                hi = m - 1
            else:
                lo = m + 1

        return result

    last = bst(arr, num, False)
    first = bst(arr, num, True)

    return last - first + 1


def findRotate(A, lo, hi, x):
    while lo <= hi:
        m = lo + (hi - lo) // 2
        if A[m] == x:
            return m
        elif A[m] <= A[hi]:
            if x <= A[hi] and x > A[m]:
                lo = m + 1
            else:
                hi = m - 1
        elif A[m] >= A[lo]:
            if x >= A[lo] and x < A[m]:
                hi = m - 1
            else:
                lo = m + 1
        else:
            return -1

    return -1


A = [5, 6, 7, 10, 1, 2, 3, 4]
print(findRotate(A, 0, len(A) - 1, 5))


class Solution:

    # Given two arrays, write a function to compute their intersection.
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        max_1 = len(nums1) - 1
        max_2 = len(nums2) - 1
        if max_1 < max_2:
            nums1.sort()
            s = nums1
            l = nums2
        else:
            nums2.sort()
            s = nums2
            l = nums1

        def binarySearch(A, start, ending, num):
            if start > ending:
                return -1
            m = round((start + ending) / 2)
            if num == A[m]:
                return m
            elif num < A[m]:
                return binarySearch(A, start, m - 1, num)
            else:
                return binarySearch(A, m + 1, ending, num)

        for x in l:
            r = binarySearch(s, 0, len(s)-1, x)
            if r >= 0 and x in s:
                res.append(x)
                s.pop(r)
            else:
                continue

        return res


# sols=Solution()
# ans = sols.intersect([1,2,2,1],[2,2])
# print(ans)
print(binarySearch_iter([2,3,4,5,7], 0, len([2,3,4,5,7]), 7))