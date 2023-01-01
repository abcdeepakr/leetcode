def sort_sorted_arr(arr1, arr2):
    p = q = 0
    sorted = []
    while (p < len(arr1) and q < len(arr2)):
        if (arr1[p] < arr2[q]):
            sorted.append(arr1[p])
            p += 1
        else:
            sorted.append(arr2[q])
            q += 1

    if (p < len(arr1)):
        for i in range(p, len(arr1)):
            sorted.append(arr1[i])
    if (q < len(arr2)):
        for i in range(q, len(arr2)):
            sorted.append(arr2[i])
    return sorted


# op = sort_sorted_arr([1, 4, 5, 8], [1, 1, 2, 2, 2, 3, 3, 3, 6, 7, 7, 7])
# print("op len", len(op))
# print(op)


def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    print('arr', arr)
    print("left", left)
    print("right", right)
    return sort_sorted_arr(left, right)


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge_sort(arr))
