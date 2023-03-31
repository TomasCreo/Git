def count_larger_than_previous(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1
    return count

array = [8, -1, 5, 2, 3]

print(count_larger_than_previous(array))
