
def selectionSort(arr):
    # @param A : list of integers
    # @return a sorted list of integers
    # time complexity - O(n^2) - Best Case
    # space complexity - Constant
    arr_size = len(arr)
    if arr_size <= 1:
        return arr

    for i in range(arr_size - 1):

        min_i = i

        for j in range(i, arr_size):
            # selection
            if arr[j] < arr[min_i]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


# print(selectionSort([2, 7, 4, 1, 5, 3]))

def bubbleSort(arr):
    # @param A : list of integers
    # @return a sorted list of integers
    # time complexity - O(n^2)
    # space complexity - Constant
    # Best case  - O(n)
    # Worst case - O(n^2)
    arr_size = len(arr)
    for i in range(arr_size):
        # k = 0
        # j loop can be improved by running to the sorted part only i.e arr_size - 1 at each iteration (i, arr_size-1-k)
        # You can improve it by using a flag to check if there no swap and break out of the loop sooner
        for j in range(i, arr_size-1):
            # swap
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # k+=1
    return arr


# print(bubbleSort([2, 7, 4, 1, 5, 3]))

def insertionSort(arr):
    # @param A : list of integers
    # @return a sorted list of integers
    # time complexity - O(n^2)
    # space complexity - Constant
    # Best case  - O(n)
    # Worst case - O(n^2)
    arr_size = len(arr)
    for i in range(arr_size):

        val = arr[i]
        hole = i
        # replace position (hole) of the current item in the sorted part of the list with its right position
        while hole > 0 and arr[hole - 1] > val:
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = val
    return arr


print(insertionSort([2, 7, 4, 1, 5, 3]))


def mergeSort(arr, n):
    # @param A : list of integers, array size
    # @return a sorted list of integers
    # time complexity - O(nlogn)
    # space complexity - O(n)
    # Best case  - O(n)
    # Worst case - O(nlogn)
    # Not in place
    if n < 2:
        return arr
    else:
        m = round(n / 2)
        left_arr = arr[:m]
        right_arr = arr[m:]

        mergeSort(left_arr, m)
        mergeSort(right_arr, n - m)

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):

            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1

            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

        return arr


def quickSort(A, start, end):
    # @param A : list of integers, array size
    # @return a sorted list of integers
    # time complexity - O(nlogn)
    # space complexity - O(logn) ~ Constant
    # Best case  - O(n)
    # Worst case - O(nlogn)
    # Not Stable
    # in place
    def partition(A, start, end):
        pivot = A[end]
        pIndex = start
        for i in range(start, end):
            if A[i] <= pivot:
                A[i], A[pIndex] = A[pIndex], A[i]
                pIndex += 1
        A[pIndex], A[end] = A[end], A[pIndex]
        return pIndex

    if start < end:
        pIndex = partition(A, start, end)
        quickSort(A, start, pIndex - 1)
        quickSort(A, pIndex + 1, end)
    return A
