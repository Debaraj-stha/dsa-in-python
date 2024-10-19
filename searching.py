def linaersearching(arr):
    l = len(arr)
    for i in range(l):
        if arr[i] == 3:
            return i
    return -1


def binary_search(arr, l, h, key):
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            h = mid - 1
        else:
            l = mid + 1
    return -1


def recursive_binary_search(arr, l, h, key):
    if l <= h:
        mid = (l + h) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return recursive_binary_search(arr, mid + 1, h, key)
        else:
            return recursive_binary_search(arr, l, mid - 1, key)
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = linaersearching(arr)
    if result != -1:
        print(f"Element 3 is found at index {result}")
    else:
        print("Element not found")

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = binary_search(l, 0, len(l), 7)
    if x == -1:
        print("Element not found")
    else:
        print("Element found at index", x)

    x = recursive_binary_search(l, 0, len(l) - 1, 7)
    if x == -1:
        print("Element not found")

    else:
        print("Element found at index", x)
