def linaersearching(arr):
    l=len(arr)
    for i in range(l):
        if arr[i]==3:
            return i
    return -1


def binarysearching(arr,key):
    l=len(arr)
    mid=l//2
    if l==1:
        return 
    elif key==arr[mid]:
        return mid
    elif key<arr[mid]:
        return binarysearching(arr[:mid],key)
    elif key>arr[mid]:
        return binarysearching(arr[mid+1:],key)
    
    return -1
    




if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = linaersearching(arr)
    if result != -1:
        print(f'Element 3 is found at index {result}')
    else:
        print('Element not found')
    
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 8
    result = binarysearching(arr, key)
    if result != -1:
        print(f'Element {key} is found at index {result}')
    else:
        print(f'Element {key} not found')