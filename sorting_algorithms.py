def insertionsort(arr):
    l=len(arr)
    for i in range(1,l):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j] :
                arr[j+1]=arr[j]
                j -= 1
        arr[j+1]=key
        
        
def selection(arr):
    l=len(arr)
    for i in range(l):
        min_idx=i
        for j in range(i+1,l):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
        
        
        
def bubblesort(arr):
    l=len(arr)
    for i in range(l):
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1] :
                arr[j], arr[j+1]=arr[j+1], arr[j]




def merge(arr,p,q,r):
    n1=q-p+1
    n2=r-q
    
    left=[0]*n1
    right=[0]*n2
    
    for i in range(0,n1):
        left[i]=arr[p+i]
    for i in range(0,n2):
        right[i]=arr[q+1+i]
        
    i=j=0
    left.append(float("inf"))
    right.append(float("inf"))
    
    for k in range(p,r+1):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
    

def mergesort(arr,p,r):
    if p<r:
        q=(p+r)//2
        mergesort(arr,p,q)
        mergesort(arr,q+1,r)
        merge(arr,p,q,r)
        
        

        

def partition(l,p,r):
    x=l[p]
    i=p-1
    for j in range(p,r):
        if l[j]<x:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[r]=l[r],l[i+1]
    return i+1
    
def quick_sort(l,p,r):
    if p<r:
        q=partition(l,p,r)
        quick_sort(l,p,q-1)
        quick_sort(l,q+1,r)


        
    

if __name__=='__main__':
    arr=[64, 34, 25, 12, 22, 11, 90]
    print('Original Array:',arr)
    insertionsort(arr)
    print('Sorted Array:',arr)
    
    arr=[64, 34, 2, 4, 636, 1, 90]
    print('Original Array:',arr)
    selection(arr)
    print('Sorted Array:',arr)
    
    arr=[64, 34, 1825, 12, 2, 11, 100]
    print('Original Array:',arr)
    bubblesort(arr)
    print('Sorted Array:',arr)
    
    
    arr=[64, 3, 25, 2, 22, 1, 90]
    print('Original Array:"',arr)
    mergesort(arr,0,len(arr)-1)
    print('Sorted Array:',arr)
    
    
    a=[64, 3, 25, 12, 2, 122, 9]
    
    print('Original Array:',a)
    quick_sort(a,0,len(a)-1)
    print('Sorted Array:',a)
    