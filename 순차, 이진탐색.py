# 순차탐색
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i


# 이진탐색 (재귀 버젼)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# 이진탐색 (반복문 버젼)
def binary_search_iter(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
