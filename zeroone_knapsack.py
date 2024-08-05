def zero_one(wt,val,w,n):
    if w==0 or n==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    if wt[n-1]<=w:
        t[n][w]=max(val[n-1]+zero_one(wt,val,w-wt[n-1],n-1),zero_one(wt,val,w,n-1))
        return t[n][w]
    elif wt[n-1]>w:
        t[n][w]=zero_one(wt,val,w,n-1)
        return t[n][w]



if __name__ == '__main__':
    wt = [4, 1, 6]
    val = [60, 100, 120]
    w =6
    n = len(wt)
    t=[[-1 for i in range(w+1)] for j in range(n+1)]
    print(zero_one(wt, val, w, n))