hashmap = {}


def merge_sorted_arrays(arr1, arr2):
    sorted_arr = []
    p = q = 0
    while (p < len(arr1) and q < len(arr2)):
        if (hashmap[arr1[p]] > hashmap[arr2[q]]):
            sorted_arr.append(arr1[p])
            p += 1
        else:
            sorted_arr.append(arr2[q])
            q += 1
    if (p < len(arr1)):
        for i in range(p, len(arr1)):
            sorted_arr.append(arr1[p])
            p += 1
    if (q < len(arr2)):
        for i in range(q, len(arr2)):
            sorted_arr.append(arr2[q])
            q += 1
    return sorted_arr


def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    return merge_sorted_arrays(left, right)


nums = [1, 1, 1, 2, 2, 3]

for i in nums:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1
print(hashmap)
keys = list(hashmap.keys())
sortedArr = merge_sort(keys)
print('sorted', sortedArr)
for i in sortedArr:
    print(i, hashmap[i])
