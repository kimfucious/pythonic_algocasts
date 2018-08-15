# --- Directions
# Implement bubbleSort, selectionSort, and mergeSort


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                bigger = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = bigger
    return arr


def selection_sort(arr):
    for i in range(0, len(arr)):
        index_of_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index_of_min]:
                index_of_min = j
        if i != index_of_min:
            bigger = arr[i]
            arr[i] = arr[index_of_min]
            arr[index_of_min] = bigger
    return arr


def merge_sort(arr):
    from math import floor

    if len(arr) == 1:
        return arr

    midpoint = floor(len(arr)/2)
    left = list(arr[0: midpoint])
    right = list(arr[midpoint:])

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    results = []
    while len(left) and len(right):
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    return[*results, *left, *right]
