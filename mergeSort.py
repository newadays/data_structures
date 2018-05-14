def mergeSort(arr, n):
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



A = [2,4,3,1]
print(mergeSort(A,4))