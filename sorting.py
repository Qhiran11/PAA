"""
pseudo code :


MergeSort(A, left, right)
    if left < right
        mid = (left + right) / 2
        MergeSort(A, left, mid)
        MergeSort(A, mid + 1, right)
        Merge(A, left, mid, right)

Merge(A, left, mid, right)
    n1 = mid - left + 1
    n2 = right - mid
    create arrays L[1...n1] and R[1...n2]
    
    for i = 1 to n1
        L[i] = A[left + i - 1]
    for j = 1 to n2
        R[j] = A[mid + j]
    
    i = 1, j = 1, k = left
    while i <= n1 and j <= n2
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else
            A[k] = R[j]
            j = j + 1
        k = k + 1

    while i <= n1
        A[k] = L[i]
        i = i + 1
        k = k + 1

    while j <= n2
        A[k] = R[j]
        j = j + 1
        k = k + 1

        

BubbleSort(A)
    n = length(A)
    for i = 0 to n-1
        for j = 0 to n-i-2
            if A[j] > A[j+1]
                swap A[j] and A[j+1]

"""





import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return X



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


X = random.sample(range(1, 100), 20)

print(f"Niali x awal\n : {X} \n")


start_time1 = time.time()
merge_sort(X)
end_time1 = time.time()


start_time2 = time.time()
bubble_sort(X)
end_time2 = time.time()
print(f"Niali x setelah di sort \n: {X} \n")

print(f"Bubble Sort Time: {end_time2 - start_time2} seconds")
print(f"Merge Sort Time: {end_time1 - start_time1} seconds")
