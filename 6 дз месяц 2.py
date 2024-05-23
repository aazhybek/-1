def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, x):
    first, last = 0, len(arr) - 1
    result_ok = False
    pos = -1

    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == x:
            result_ok = True
            pos = middle
            break
        elif arr[middle] < x:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f"Элемент {x} найден на позиции:", pos)
    else:
        print(f"Элемент {x} не найден")
    return pos


unsorted_list = [74, 39, 35, 12, 22, 11, 50]
print("Неотсортированный список:", unsorted_list)

sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список (пузырьковая сортировка):", sorted_list)

element_to_search = 22
result = binary_search(sorted_list, element_to_search)