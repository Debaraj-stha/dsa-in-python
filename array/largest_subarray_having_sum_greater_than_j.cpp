#include<iostream>
#include<vector>
#include<climits>  // For INT_MAX

using namespace std;

void display(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
void swap(int *a,int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sort(vector<vector<int>> arr,int n){
    for(int i=0;i<n;i++) {
        for(int j=0;j<n-i-1;j++) {
            if(arr[0][j]>arr[0][j+1]) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}
int findInd(vector<vector<int>> Presum,int val)
{
    int l=0, r=Presum.size()-1;
    while(l<r){
        int mid = l + (r-l)/2;
        if(Presum[mid][0]>=val) r=mid;
        else l=mid+1;
    }
    return Presum[l][0]==val?l:-1;
}
int findLargestSumSubarrayGreaterThanK(int * arr,int n,int X){
    int result=0;
    vector<vector<int>> Presum;
    int sum=0;
    for (int i=0;i<n;i++){
        sum+=arr[i];
        Presum.push_back({sum,i});
    }
    sort(Presum,Presum.size());
    vector<int> minIndex(n,0);
    minIndex[0]=Presum[0][1];
    for(int i=0;i<n;i++){
        minIndex[i]=min(minIndex[i-1],Presum[i][1]);
    }
    sum = 0;
    for(int i=0;i<n;i++){
        sum += arr[i];
        if(sum>X){
            result = i + 1;
        }
        else{
            int ind = findInd(Presum, sum-X-1);
            if(ind!=-1 && minIndex[ind]<i){
                result = max(result,i - minIndex[ind]);
            }
        }
        
    }
    

    return result;

}
int main() {
   int arr[] = {2, -3, 3, 2, 0, -1};
   int n = sizeof(arr)/sizeof(arr[0]);
   int k = 3;
    display(arr, n);
    cout << "largest subarray  having sum greater than  "<<k << "=" << findLargestSumSubarrayGreaterThanK(arr, n, k) << endl;

    return 0;
}
