def min_max(arr,i,j):
    min1=max1=0
    if i==j:
        global min0,max0
        min0=max0=arr[i]
        
    elif i==j-1:
        if arr[i]<arr[j]:
            min0=arr[i]
            max0=arr[j]
        else:
            min0=arr[j]
            max0=arr[i]
    else:
        mid=(i+j)//2
        min_max(arr,i,mid)
        min1=min0
        max1=max0
        min_max(arr,mid+1,j)
        if min0>min1:
            min0=min1
        if max0<max1:
            max0=max1
            
            
            
if  __name__ == "__main__":
    
    
    arr=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    min0=max0=0
    min_max(arr,0,len(arr)-1)
    print("Minimum:",min0)
    print("Maximum:",max0)
        