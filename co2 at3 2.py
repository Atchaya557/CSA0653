def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j # ERROR
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
print(selection_sort([64, 25, 22, 22, 11]))
