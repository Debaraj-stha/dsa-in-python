def min_max(arr,i,j):
    if i==j:
        return arr[i],arr[i]
    elif i==j-1:
        if arr[i]<arr[j]:
            return arr[i],arr[j]
        else:
            return arr[j],arr[i]
    else:
        mid=(i+j)//2
        min1,max1=min_max(arr,i,mid)
        min2,max2=min_max(arr,mid+1,j)
        min_val,max_val=min(min1,min2),max(max2,max1)
        return min_val,max_val
arr=[4,8,3,22,12,11,1]
min_max(arr,0,len(arr)-1)

    