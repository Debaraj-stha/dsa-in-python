def heapify(lists, i):
    global heapsize
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < heapsize and lists[l] > lists[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and lists[r] > lists[largest]:
        largest = r
    if largest != i:
        lists[i], lists[largest] = lists[largest], lists[i]
        heapify(lists, largest)


def buildheap(lists):
    global heapsize
    heapsize = len(lists)
    start = heapsize // 2 - 1
    for i in range(start, -1, -1):
        heapify(lists, i)


def heapsort(lists):
    global heapsize
    buildheap(lists)
    for i in range(heapsize - 1, 0, -1):
        lists[i], lists[0] = lists[0], lists[i]
        heapsize -= 1
        heapify(lists, 0)


if __name__ == "__main__":
    arr = [12, 1, 6, 8, 9, 3, 2]
    print("Original Array:", arr)
    heapsort(arr)
    print("Sorted Array:", arr)
